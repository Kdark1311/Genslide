import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import json
import os
import datetime
import urllib.parse # Thư viện để mã hóa URL ảnh

# --- 1. CẤU HÌNH API KEY ---
GOOGLE_API_KEY = "AIzaSyBh6HVUbzhlAsOBUtNoy7AA3ULs1WRSXpM"

# --- 2. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(layout="wide", page_title="Voice-to-Slide Prototype")

st.markdown("""
<style>
    .slide-container {
        background-color: white;
        color: black;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        height: 700px; /* Tăng chiều cao để chứa ảnh */
        display: flex;
        flex-direction: column;
        justify_content: flex-start;
        border: 1px solid #ddd;
    }
    .slide-title {
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 20px;
        color: #1a202c;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 10px;
    }
    .slide-content {
        font-size: 24px;
        line-height: 1.5;
        color: #2d3748;
        margin-bottom: 20px;
    }
    .slide-content li {
        margin-bottom: 10px;
    }
    .visual-box {
        margin-top: auto;
        border-radius: 10px;
        overflow: hidden;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    .visual-box img {
        width: 100%;
        height: 300px;
        object-fit: cover;
    }
    .log-box {
        background-color: #0e1117;
        color: #00ff00;
        font-family: 'Courier New', monospace;
        padding: 10px;
        border-radius: 5px;
        height: 200px;
        overflow-y: scroll;
        font-size: 12px;
        border: 1px solid #333;
    }
    .stButton>button {
        width: 100%;
        font-size: 16px;
        border-radius: 8px;
        height: 45px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. KHỞI TẠO TRẠNG THÁI ---
if "current_slide" not in st.session_state:
    st.session_state.current_slide = {
        "title": "Voice Presentation AI",
        "points": ["Hệ thống đã sẵn sàng.", "Nội dung sẽ được AI mở rộng chi tiết hơn."],
        "visual_desc": "abstract technology background, blue and white, minimal, 4k", # Mặc định tiếng Anh để tạo ảnh đẹp
        "theme_color": "#ffffff"
    }

if "voice_text_draft" not in st.session_state:
    st.session_state.voice_text_draft = ""

if "system_logs" not in st.session_state:
    st.session_state.system_logs = ["--- System Started ---"]

# Biến lưu tên model tìm thấy được
if "valid_model_name" not in st.session_state:
    st.session_state.valid_model_name = None

def log_to_ui(message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    st.session_state.system_logs.append(log_entry)

# --- 4. HÀM KIỂM TRA KẾT NỐI ---
def check_connection():
    log_to_ui("--- DEBUG: Checking API Connection ---")
    try:
        clean_key = GOOGLE_API_KEY.strip()
        if "DÁN_API_KEY" in clean_key or not clean_key:
            st.error("⚠️ Bạn chưa dán API Key vào code!")
            return

        genai.configure(api_key=clean_key)
        log_to_ui("Listing models...")
        models = list(genai.list_models())
        valid_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
        
        if not valid_models:
            st.error("Không tìm thấy model nào hỗ trợ tạo nội dung.")
            return

        selected_model = valid_models[0]
        for m in valid_models:
            if 'gemini-2.5-flash' in m:
                selected_model = m
                break
            elif 'gemini-1.5-flash' in m:
                selected_model = m
        
        st.session_state.valid_model_name = selected_model
        
        log_to_ui(f"✅ FOUND {len(valid_models)} MODELS.")
        log_to_ui(f"👉 SELECTED MODEL: {selected_model}")
        st.toast(f"Đã chọn model: {selected_model}", icon="🤖")
            
    except Exception as e:
        log_to_ui(f"FATAL ERROR: {e}")
        st.error(f"Lỗi kết nối: {e}")

# --- 5. HÀM NHẬN DIỆN GIỌNG NÓI ---
def listen_to_voice():
    r = sr.Recognizer()
    r.energy_threshold = 300 
    r.dynamic_energy_threshold = True
    r.pause_threshold = 2.0 
    
    with sr.Microphone() as source:
        status = st.empty()
        status.info("🎤 Đang nghe... (Chế độ không ngắt lời)")
        log_to_ui("Mic: Listening...")
        
        try:
            r.adjust_for_ambient_noise(source, duration=1.0)
            audio_data = r.listen(source, timeout=None, phrase_time_limit=None)
            
            status.warning("⏳ Đang xử lý âm thanh...")
            log_to_ui("Mic: Converting to text...")
            
            text = r.recognize_google(audio_data, language="vi-VN")
            log_to_ui(f"User Said: {text}")
            status.empty()
            return text
            
        except sr.UnknownValueError:
            status.error("Không nghe rõ lời nói.")
            log_to_ui("Error: Audio not clear.")
            return None
        except Exception as e:
            status.error(f"Lỗi Micro: {e}")
            log_to_ui(f"Mic Error: {e}")
            return None

# --- 6. HÀM GỌI GEMINI (PROMPT NÂNG CAO) ---
def update_slide_with_ai(user_input, current_slide_state):
    log_to_ui(f"Sending: '{user_input}'")
    try:
        clean_key = GOOGLE_API_KEY.strip()
        if not clean_key:
            st.error("Chưa nhập API Key!")
            return current_slide_state
        
        if not st.session_state.valid_model_name:
             check_connection()
             if not st.session_state.valid_model_name:
                 st.error("Không tìm thấy model AI.")
                 return current_slide_state

        target_model = st.session_state.valid_model_name
        genai.configure(api_key=clean_key)
        
        model = genai.GenerativeModel(target_model, generation_config={"response_mime_type": "application/json"})
        
        # --- PROMPT NÂNG CAO ---
        # Yêu cầu AI đóng vai chuyên gia thiết kế và viết prompt ảnh bằng tiếng Anh
        prompt = f"""
        Bạn là một Chuyên Gia Thiết Kế Bài Thuyết Trình Đẳng Cấp Thế Giới (World-class Presentation Designer).
        
        INPUT:
        1. Slide hiện tại (JSON): {json.dumps(current_slide_state)}
        2. Lời người dùng: "{user_input}"
        
        NHIỆM VỤ:
        1. Phân tích ý định người dùng (Tạo mới, bổ sung, hay sửa đổi).
        2. Nâng cấp nội dung: 
           - Nếu người dùng nói ngắn gọn, hãy BỔ SUNG chi tiết chuyên sâu, mở rộng thành các gạch đầu dòng có ý nghĩa.
           - Sử dụng ngôn ngữ chuyên nghiệp, gãy gọn.
        3. Tạo Prompt hình ảnh (QUAN TRỌNG):
           - Trường 'visual_desc' PHẢI viết bằng TIẾNG ANH (English).
           - Mô tả chi tiết, nghệ thuật để AI vẽ tranh hiểu được (Ví dụ: "futuristic medical robot doctor, cinematic lighting, 4k, photorealistic").
        
        Output JSON format:
        {{
            "title": "Tiêu đề ấn tượng (Tiếng Việt)",
            "points": ["Ý chính 1 (Chi tiết)", "Ý chính 2 (Chi tiết)", ...],
            "visual_desc": "English description for image generation (keywords, style)",
            "theme_color": "hex_code (chọn màu nhã nhặn phù hợp chủ đề)"
        }}
        """
        
        log_to_ui(f"Using Model: {target_model}")
        response = model.generate_content(prompt)
        log_to_ui("Success! Response received.")
        return json.loads(response.text)
            
    except Exception as e:
        st.error(f"Lỗi AI: {e}")
        log_to_ui(f"AI Error: {e}")
        if "404" in str(e):
            st.session_state.valid_model_name = None
        return current_slide_state

# --- 7. GIAO DIỆN CHÍNH ---
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🎛️ Bảng điều khiển")
    
    if st.button("🔌 Khởi động & Tìm Model"):
        check_connection()
        if st.session_state.valid_model_name:
             st.success(f"Đang dùng: {st.session_state.valid_model_name}")
    
    st.markdown("---")
    
    st.write("### 1. Thu âm")
    st.caption("Micro sẽ nghe liên tục (chờ im lặng 2s).")
    if st.button("🎙️ BẮT ĐẦU NÓI", type="primary"):
        text = listen_to_voice()
        if text:
            st.session_state.voice_text_draft = text
            st.rerun()

    st.write("### 2. Gửi lệnh")
    final_input = st.text_area("Nội dung:", value=st.session_state.voice_text_draft, height=80)

    if st.button("🚀 XỬ LÝ (SEND)"):
        if final_input.strip():
            with st.spinner("AI đang thiết kế lại slide và vẽ ảnh..."):
                new_slide = update_slide_with_ai(final_input, st.session_state.current_slide)
                st.session_state.current_slide = new_slide
                st.session_state.voice_text_draft = ""
                st.rerun()

    st.markdown("---")
    st.write("### 📟 Logs")
    logs = "\n".join(st.session_state.system_logs[::-1])
    st.markdown(f'<div class="log-box">{logs}</div>', unsafe_allow_html=True)

with col2:
    st.header("🖥️ Màn hình trình chiếu")
    slide = st.session_state.current_slide
    
    # --- XỬ LÝ HÌNH ẢNH ---
    # Mã hóa prompt tiếng Anh để đưa vào URL
    encoded_visual_prompt = urllib.parse.quote(slide['visual_desc'])
    # Sử dụng Pollinations.ai (Free API) để tạo ảnh từ prompt
    image_url = f"https://image.pollinations.ai/prompt/{encoded_visual_prompt}?width=800&height=400&nologo=true"

    html = f"""
    <div class="slide-container" style="background-color: {slide.get('theme_color', '#ffffff')};">
        <div class="slide-title">{slide['title']}</div>
        <div class="slide-content">
            <ul>{''.join(f'<li>{p}</li>' for p in slide['points'])}</ul>
        </div>
        <div class="visual-box">
            <img src="{image_url}" alt="AI generated Image" />
            <p style="font-size: 12px; margin-top: 5px; color: #666;">Prompt: {slide['visual_desc']}</p>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    with st.expander("JSON Data"):
        st.json(slide)