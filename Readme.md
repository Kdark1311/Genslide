# NGHIÊN CỨU VÀ XÂY DỰNG HỆ THỐNG TRỰC QUAN HÓA BÀI THUYẾT TRÌNH THEO THỜI GIAN THỰC DỰA TRÊN GIỌNG NÓI VÀ GENERATIVE AI

**Development of a Real-time Voice-to-Slide Presentation System using Generative AI with Streaming UI and Voice-based Dual-Mode Interaction**

---

**Sinh viên thực hiện:** [Tên của bạn]  
**MSSV:** [Mã số sinh viên]  
**Giảng viên hướng dẫn:** [Tên giảng viên]  
**Khoa/Bộ môn:** [Tên khoa]  
**Ngày nộp:** [Ngày/Tháng/Năm]

---

## MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Tổng quan tài liệu](#2-tổng-quan-tài-liệu)
3. [Phương pháp nghiên cứu](#3-phương-pháp-nghiên-cứu)
4. [Kế hoạch đánh giá](#4-kế-hoạch-đánh-giá)
5. [Kết quả dự kiến](#5-kết-quả-dự-kiến)
6. [Timeline & Milestones](#6-timeline--milestones)
7. [Rủi ro & Giải pháp](#7-rủi-ro--giải-pháp)
8. [Đóng góp khoa học](#8-đóng-góp-khoa-học)
9. [Hạn chế & Hướng phát triển](#9-hạn-chế--hướng-phát-triển)
10. [Kết luận](#10-kết-luận)
11. [Tài liệu tham khảo](#11-tài-liệu-tham-khảo)

---

## 1. GIỚI THIỆU

### 1.1. Đặt vấn đề

Trong kỷ nguyên số hóa, việc thuyết trình đóng vai trò then chốt trong giáo dục, kinh doanh và nghiên cứu. Tuy nhiên, quy trình tạo slide thuyết trình truyền thống (PowerPoint, Google Slides) tồn tại nhiều hạn chế nghiêm trọng:

#### Vấn đề 1: Gián đoạn tư duy (Cognitive Flow Interruption)

Khi soạn slide thủ công, người dùng phải:
- Chuyển đổi liên tục giữa "suy nghĩ nội dung" và "thiết kế giao diện"
- Dừng dòng chảy tư duy để thao tác chuột, bàn phím
- Mất focus vào formatting thay vì content

**Hậu quả:** 
- Chất lượng nội dung giảm
- Thời gian tăng (trung bình 3-5 phút/slide)
- Stress và mệt mỏi

#### Vấn đề 2: Công cụ AI thiếu tính tương tác thời gian thực

Các công cụ AI hiện nay (Gamma.ai, Tome.app, SlidesAI) hoạt động theo **"Batch Processing"**:

```
User nhập đầy đủ content → Chờ đợi xử lý → Nhận kết quả hoàn chỉnh
```

**Hạn chế:**
- ❌ Không phù hợp với **brainstorming** (lên ý tưởng tự nhiên)
- ❌ Không cho phép **điều chỉnh trong quá trình** tạo
- ❌ Thiếu **feedback tức thì** → Không biết system có hiểu đúng không
- ❌ **Phải chuẩn bị content xong** mới bắt đầu → Mất tính tự phát

#### Vấn đề 3: Thiếu nghiên cứu về Voice-First Authoring

Hiện nay chưa có nhiều nghiên cứu học thuật về:
- **Real-time streaming** từ speech sang visual content
- **Voice-only interaction** (100% giọng nói, không keyboard/mouse)
- **Incremental rendering** (nội dung xuất hiện dần, không chờ đợi)
- **Dual-mode voice interaction** (sáng tạo vs chỉnh sửa)

**Research Gap:** Các nghiên cứu hiện có (PASS, PresentAgent) focus vào document-to-slides, **KHÔNG có** hệ thống speech-to-slides real-time.

---

### 1.2. Nhu cầu thực tế

#### Use Cases

**👨‍🏫 Giáo dục:**
- Giáo viên chuẩn bị bài giảng từ ghi chú nhanh
- Sinh viên tạo slide thuyết trình đồ án
- Gia sư chuẩn bị tài liệu giảng dạy

**💼 Doanh nghiệp:**
- Brainstorming session → Visual slides ngay lập tức
- Sales pitch creation trong meeting
- Quick deck cho client presentation

**📊 Nghiên cứu:**
- Researcher chuẩn bị conference talk
- Lab meeting slides từ experiment notes
- Visual aids cho paper presentation

**🎤 Diễn giả:**
- Improvised presentations
- Rapid prototyping của talk ideas
- On-the-fly slide creation during Q&A

**♿ Accessibility:**
- Người khuyết tật tay/ngón tay
- Repetitive strain injury (RSI) sufferers
- Visual impairment (voice-first = eyes-free)

#### Đặc điểm lý tưởng của công cụ

Một công cụ lý tưởng cần:
1. ⚡ **Phản hồi tức thì**: Nội dung xuất hiện < 2 giây
2. 🎬 **Streaming UI**: Content "mọc lên" dần (như Gamma.app)
3. 🗣️ **Voice-only**: 100% giọng nói, không cần tay
4. 🎯 **Dual-mode**: Sáng tạo tự nhiên + Chỉnh sửa chính xác
5. 📊 **Chất lượng cao**: Comparable với AI tools hiện có

→ **GenSlide** được thiết kế để đáp ứng tất cả nhu cầu trên.

---

### 1.3. Mục tiêu nghiên cứu

Đề tài nhằm xây dựng hệ thống phần mềm (Web Application) với các mục tiêu cụ thể:

#### Mục tiêu 1: Real-time Streaming Architecture
- **Speech Layer**: Streaming ASR với two-pass decoding (preview 300ms + accurate 1.5s)
- **Language Layer**: Streaming LLM response token-by-token
- **Render Layer**: Incremental DOM updates với animations
- **Target latency**: < 2 seconds end-to-end

#### Mục tiêu 2: Dual-Mode Voice Interaction
- **Brainstorming Mode**: 
  - User nói tự nhiên: "Hôm nay tôi muốn nói về AI trong y tế..."
  - System tự hiểu và tạo slide structure
  - No explicit commands needed
  
- **Editing Mode**:
  - User ra lệnh: "Sửa tiêu đề thành...", "Xóa bullet thứ 2"
  - System parse commands và execute
  - Context-aware ("cái đó", "slide này")

- **Mode Switching**: Mượt mà bằng button click

#### Mục tiêu 3: Streaming UI Experience
- Nội dung xuất hiện **dần dần** (Title → Bullet 1 → Bullet 2...)
- **Không** chờ đợi rồi "bật lên" (wait-then-pop)
- Animations: Typewriter effect, Fade-in, Slide-up
- Maintain 60 FPS performance

#### Mục tiêu 4: Quality Maintenance
- PresentEval Content Fidelity: > 8.0/10
- Visual Clarity: > 7.5/10
- Intent Classification: > 90% accuracy (Brainstorm), > 85% (Edit)
- Comparable with SOTA (PASS: 9.02/10) - acceptable 10% gap

#### Mục tiêu 5: Đóng góp khoa học
- First speech-to-slide real-time system
- Incremental JSON parsing algorithm
- Dual-mode voice interaction framework
- Benchmark protocol using SlideSpeech dataset
- Optimal update frequency guidelines (evidence-based)

---

### 1.4. Câu hỏi nghiên cứu

#### RQ1: Real-time Speech-to-Slide Streaming Alignment ⭐⭐⭐
> **"Làm thế nào đồng bộ hóa continuous speech stream với incremental slide rendering để tạo cảm giác 'đang được tạo ra' thay vì 'đợi xong xuất hiện'?"**

**Techniques cần nghiên cứu:**
- **Sliding Window ASR**: Window size optimal? 640ms từ U2 Whisper paper?
- **Two-Pass Decoding**: CTC (fast preview) + Attention (accurate final)
- **VAD with Prosody**: Kết hợp acoustic + prosody + linguistic signals
- **Word-level Timestamps**: Forced alignment cho emphasis detection

**Metrics:**
- Time to First Content (TTFC): Target < 1.5s
- Update Frequency: 5-10 updates/second
- Perceived Responsiveness: Likert 1-7 scale

**Baseline:**
- Batch mode: TTFC = 3s, 1 update total
- Streaming target: TTFC < 1.5s, 5-10 updates

**Hypothesis:** Streaming approach với two-pass decoding sẽ achieve TTFC < 2s while maintaining accuracy (WER < 10%).

---

#### RQ2: Incremental JSON Parsing for Streaming LLM ⭐⭐⭐
> **"Làm thế nào parse và render JSON structure khi nó đang được generate token-by-token từ LLM streaming API?"**

**Research Gap:**
- Existing JSON parsers: Require complete, valid JSON
- LLM streaming: Outputs tokens sequentially
- Need: Parser that works on **partial** JSON

**Techniques cần phát triển:**
- **State Machine Parser**: Track parsing state (IN_TITLE, IN_BULLETS, ...)
- **Field-level Granularity**: Có thể render title trước khi bullets ready
- **Error Recovery**: Handle invalid partial JSON gracefully
- **Buffering Strategy**: Parse every token? Every N tokens? On complete field?

**Metrics:**
- Parse success rate on partial JSONs: Target > 95%
- Latency overhead: < 10ms per token
- False positive renders: < 5% (render incomplete/wrong content)

**Novel Contribution:**
- First application of streaming JSON parsing trong interactive UI generation
- Prior work: Batch JSON parsing (PASS, PresentAgent)
- Open-source library để release

**Example:**
```
Token stream: '{"title":"AI' → Partial: {title: "AI"}
              → Renderable? YES! → UI updates
              
Token stream: ' trong Y tế",' → Complete: {title: "AI trong Y tế"}
              → Renderable? YES! → UI updates again
```

---

#### RQ3: Incremental DOM Update Optimization ⭐⭐
> **"Chiến lược nào cho incremental DOM updates mang lại trải nghiệm smooth nhất mà không gây flicker hay performance bottleneck?"**

**Approaches cần so sánh:**
- **A**: Full re-render (baseline)
- **B**: Virtual DOM diffing (React-style)
- **C**: Direct DOM + requestAnimationFrame batching
- **D**: Morphdom library

**Metrics:**
- **Frame Rate**: Target maintain 60 FPS
- **Layout Thrashing**: Count forced reflows (target < 2 per update)
- **Memory Overhead**: Virtual DOM memory usage
- **Perceived Smoothness**: User rating (Likert 1-7)

**Hypothesis:**
- Virtual DOM (B) hoặc RAF batching (C) sẽ significantly outperform full re-render (p < 0.01)
- Trade-off: B có memory overhead nhưng smoother, C ít memory nhưng cần careful coordination

**Experiment:**
- Same content, different rendering strategies
- Measure FPS, layout thrashing, user preference
- Statistical test: ANOVA + post-hoc

---

#### RQ4: Dual-Mode Voice Interaction Design ⭐⭐⭐
> **"Làm thế nào thiết kế interaction pattern cho phép user seamlessly switch giữa Brainstorming Mode (generative) và Editing Mode (imperative) chỉ bằng giọng nói?"**

**Research Gap:**
- PASS/PresentAgent: One-way (document → slides), no editing
- Gamma.ai: Manual editing only (keyboard/mouse)
- Voice assistants (Siri, Alexa): Single mode (command-based)
- **GenSlide**: Dual-mode, voice-only - **FIRST!**

**Challenges:**
1. **Intent Classification Ambiguity**
   - Brainstorm: "Thêm ý về AI" → Generate content about AI
   - Edit: "Thêm ý về AI" → Execute command "add bullet mentioning AI"
   - Same words, different meanings!

2. **Context Management**
   - "Sửa cái đó" → Which element?
   - "Xóa ý thứ 2" → Which slide? Current or previous?
   - Need context tracking

3. **Mode Switching UX**
   - How does user know current mode?
   - Visual indicators sufficient?
   - Accidental mode switches?

**Techniques:**
- **Separate LLM Prompts** per mode
- **Context Manager**: Track current slide, last mentioned element
- **Reference Resolution**: NLP for "cái đó", "ý thứ 2"
- **Visual Feedback**: Clear mode indicators

**User Study Scenarios:**
1. Brainstorm 3 slides → Switch to Edit → Modify slide 2 → Resume brainstorm
2. Complex edit: "Sửa bullet thứ 2 của slide đầu tiên thành..."
3. Ambiguous reference: "Xóa cái đó" → System should ask for clarification?

**Metrics:**
- Intent classification accuracy: Brainstorm mode > 90%, Edit mode > 85%
- Command execution success rate: > 90%
- Mode confusion rate: < 10% (user doesn't know current mode)
- User satisfaction với mode switching: Likert > 5/7

---

#### RQ5: Optimal Streaming Update Frequency ⭐⭐
> **"Tần suất cập nhật UI bao nhiêu lần/giây là tối ưu cho readability và perceived responsiveness?"**

**Hypothesis:**
Inverted U-shape relationship:
- Too slow (< 3 Hz): Choppy, feels laggy
- Too fast (> 15 Hz): Overwhelming, hard to read
- **Sweet spot: 6-10 Hz** (based on human perception research)

**Experiment Design:**
- **Type**: Within-subjects
- **Participants**: n=20
- **Conditions**: 6 levels (1Hz, 3Hz, 6Hz, 10Hz, 15Hz, 30Hz)
- **Same content**, different update rates
- **Randomized order** to control for learning effects

**Measurements:**
- **Reading Comprehension**: Recall test after each condition
- **Perceived Smoothness**: Likert 1-7 ("How smooth was the animation?")
- **Preference Ranking**: Rank conditions from best to worst

**Statistical Analysis:**
- One-way repeated measures ANOVA
- Post-hoc: Tukey HSD for pairwise comparisons
- Effect size: Partial eta-squared
- Expected: Main effect of frequency (p < 0.001), peak at 8-10Hz

**Practical Contribution:**
Evidence-based guideline cho streaming UI design, generalizable beyond presentations.

---

#### RQ6: Streaming vs Batch Quality Trade-off ⭐⭐
> **"Có sự trade-off nào giữa streaming mode (real-time) và batch mode (wait for complete) về chất lượng nội dung không?"**

**Hypothesis:**
- **H0** (null): No significant difference in quality
- **H1**: Streaming < Batch (vì LLM không "think" đủ before outputting)

**Rationale for H1:**
- Streaming: LLM outputs token-by-token → Less "thinking time"
- Batch: LLM sees full input, can plan complete response
- Trade-off: Speed vs Quality?

**Experiment:**
- **Same 100 speech inputs** (from SlideSpeech test set)
- **Condition A**: Streaming (Gemini stream=True)
- **Condition B**: Batch (Gemini stream=False)
- **Condition C**: Streaming + Polish pass (hypothesis: eliminates gap)
- **Evaluate**: PresentEval framework (Content Fidelity, Visual Clarity)

**Metrics:**
- Content Fidelity: 0-10 scale (VLM evaluation)
- Grammar errors count
- Coherence score
- User preference (blind A/B test)

**Expected Results:**
```
Condition  | Fidelity | Latency | User Pref
-----------|----------|---------|----------
A (Stream) | 7.8      | 2s      | 30%
B (Batch)  | 8.3      | 5s      | 20%
C (S+Polish)| 8.2     | 3s      | 50% ← BEST!
```

**Contribution:**
- Demonstrate polish pass as effective mitigation
- Quantify acceptable quality gap for speed gain
- Inform design decisions for real-time AI systems

---

## 2. TỔNG QUAN TÀI LIỆU

### 2.1. Công cụ hiện có

#### 2.1.1. Công cụ truyền thống

| Tool | Strengths | Limitations | Time/Slide |
|------|-----------|-------------|------------|
| PowerPoint | Full control, powerful features | Manual, steep learning curve | 3-5 min |
| Google Slides | Collaboration, cloud-based | Similar manual process | 3-5 min |
| Keynote | Beautiful design templates | macOS only, manual | 4-6 min |

**Tóm tắt:** Chất lượng cao nhưng **tốn thời gian** và **gián đoạn tư duy**.

#### 2.1.2. Công cụ AI hiện tại

**Gamma.ai:**
- ✅ Beautiful UI với streaming rendering effect
- ✅ AI-powered content generation
- ❌ **Batch input**: Paste text đầy đủ, không real-time
- ❌ **No voice**: Keyboard/mouse only
- ❌ **Manual editing**: Click và type

**Tome.app:**
- ✅ AI content generation
- ✅ Multimodal (text + images)
- ❌ Batch processing
- ❌ No voice interaction
- ❌ Wait for complete deck

**SlidesAI:**
- ✅ Simple, fast
- ❌ Limited customization
- ❌ Batch, no streaming
- ❌ No voice

**Beautiful.ai:**
- ✅ Smart templates, auto-layout
- ❌ Manual input only
- ❌ Focus on design, not speed

### 2.2. State-of-the-Art Academic Research (9 Papers)

#### Paper 1: PASS (2025) ⭐⭐⭐
**Liu et al. "Presentation Automation for Slide Generation and Speech"**

**Key Contributions:**
- Modular pipeline: Document → Titles → Content → Refinement → Script → TTS
- Multi-model comparison: GPT-4o-PASS (9.02/10) >> D2S fine-tuned (7.34/10)
- **PresentEval framework**: Content Fidelity, Visual Clarity, Coherence

**Relevance to GenSlide:**
- ✅ Modular architecture inspiring
- ✅ PresentEval metrics directly applicable
- ✅ Content generation techniques
- ❌ Direction: **Document** → Slides (GenSlide: **Speech** → Slides)
- ❌ Batch processing, not real-time
- ❌ No voice interaction

**GenSlide will adapt:**
- Modular pipeline design
- PresentEval for evaluation
- Reverse pipeline direction

---

#### Paper 2: PresentAgent (2025) ⭐⭐⭐
**Zhang et al. "Multimodal Agent for Presentation Video Generation"**

**Key Contributions:**
- **Multi-LLM ensemble** (GPT-4o + Gemini + Claude) > Single model
- Comprehensive PresentEval implementation
- Prosody-aware TTS
- Layout-aware slide composition

**Relevance to GenSlide:**
- ✅ **CRITICAL**: Multi-model routing strategy
- ✅ PresentEval framework detailed
- ✅ Multimodal generation approach
- ❌ Document-driven, not voice
- ❌ Batch processing
- ❌ Output: Video, not interactive slides

**GenSlide will adopt:**
- Multi-LLM routing (Gemini Fast vs GPT-4o vs Claude)
- PresentEval evaluation
- Layout generation techniques

---

#### Paper 3: U2 Whisper (2025) ⭐⭐⭐
**Li et al. "Adapting Whisper for Streaming ASR via Two-Pass Decoding"**

**Key Contributions:**
- Two-pass: CTC branch (200ms fast) + Attention branch (1.5s accurate)
- Streaming-friendly architecture
- Real-time factor < 1 on CPU
- Optimal chunk size: 640ms

**Relevance to GenSlide:**
- ✅ **ESSENTIAL** - Solves Whisper's streaming limitation
- ✅ Two-pass perfect for preview + final
- ✅ Low latency enables < 2s target
- ❌ English/Mandarin focus (need adapt for Vietnamese)

**GenSlide will use:**
- Two-pass decoding: Preview for UI, Final for LLM
- 640ms chunk size
- Benchmark on Vietnamese presentation domain

---

#### Paper 4: WhisperX (2023) ⭐⭐⭐
**Bain et al. "Word-level Timestamps & Diarization"**

**Key Contributions:**
- Forced alignment với Wav2Vec2 → Word-level timestamps
- 70x realtime speed với batching
- No WER degradation with VAD preprocessing

**Relevance to GenSlide:**
- ✅ **CRITICAL** - Word timestamps cho emphasis detection
- ✅ 70x speed enables real-time
- ✅ Production-ready tool
- ✅ Open-source, actively maintained

**GenSlide will use:**
- Word timestamps to detect emphasized words (speak slowly = important → bold)
- Align speech segments với slide content
- VAD for sentence boundary detection

---

#### Paper 5: SlideSpeech (2023) ⭐⭐⭐
**Xu et al. "Large-Scale Slide-Enriched Audio-Visual Corpus"**

**Key Contributions:**
- 1,705 videos, 1,000+ hours synchronized speech-slides
- 22 domains (CS, music, history, agriculture, ...)
- Benchmark dataset cho multimodal ASR

**Relevance to GenSlide:**
- ✅ **THE DATASET** - 1000+ hours perfect for evaluation
- ✅ Synchronized speech-slides = ground truth
- ✅ Cross-domain coverage
- ❌ Designed for ASR, not generation

**GenSlide will use:**
- **Evaluation benchmark** (test set: 25 videos, 8.75h)
- Learn slide patterns from training data
- Baseline comparison với human-created slides

---

#### Paper 6: Few-shot Style Transfer (2022) ⭐⭐
**Krishnan et al. "Few-shot Style Transfer for Multilingual Settings"**

**Key Contributions:**
- Style transfer với chỉ 3-10 examples (no large corpus needed)
- Paraphrase-based style modeling
- Controllable magnitude (0-1 scalar)

**Relevance to GenSlide:**
- ✅ Personalization với minimal examples
- ✅ No retraining needed
- ❌ Text style only, not visual/layout

**GenSlide future extension:**
- Learn user's slide style từ 5-10 examples
- Apply style preferences automatically
- Controllable style strength

---

#### Paper 7-9: Supporting Papers ⭐

**LayoutLMv3** (Huang et al. 2022):
- Joint text-layout understanding
- Could analyze user's example slides

**PosterLLaVa** (Li et al. 2024):
- LLM generates layouts (bounding boxes)
- Content-aware approach

**Auto-Slides** (Chen et al. 2023):
- Multi-agent collaboration (Parser, Verifier, Repair)
- Interactive refinement

**GenSlide potential use:**
- Layout understanding from examples
- LLM-based layout generation
- Quality verification-repair loop

---

### 2.3. Research Gap - Bảng so sánh

| Aspect | Existing Work | **GenSlide Contribution** |
|--------|---------------|---------------------------|
| **Input** | Document (PASS, PresentAgent) | **Speech (real-time)** |
| **Processing** | Batch (wait for complete) | **Streaming (continuous)** |
| **Interaction** | One-way (input → output) | **Dual-mode (Brainstorm ↔ Edit)** |
| **UI** | Static (wait then appear) | **Streaming UI (gradual)** |
| **Latency** | 30s - 2 minutes | **< 2 seconds** |
| **Editing** | Manual (keyboard/mouse) or No editing | **Voice-only commands** |
| **Modality** | Text/Document input | **Voice-first, voice-only** |
| **Evaluation** | Document-based | **Speech-to-slide (new)** |

**Key Novel Contributions:**

1. ✅ First real-time speech-to-slide system với streaming architecture
2. ✅ First voice-only dual-mode interaction (Brainstorm vs Edit)
3. ✅ First application of streaming LLM cho structured data generation
4. ✅ Incremental JSON parsing algorithm
5. ✅ Benchmark protocol for speech-to-slide using SlideSpeech
6. ✅ Evidence-based optimal update frequency guidelines

---

## 3. PHƯƠNG PHÁP NGHIÊN CỨU

### 3.1. Phương pháp tiếp cận

**Research Paradigm:** Design Science Research + Experimental Evaluation

**Quy trình 4 bước:**

1. **Design & Build** (Weeks 1-6):
   - Thiết kế streaming architecture
   - Implement prototype với core features
   - Iterative development + testing

2. **Demonstrate** (Week 7):
   - Demo scenarios covering key use cases
   - Pilot testing với 5 users
   - Identify major bugs

3. **Evaluate** (Weeks 8-11):
   - Benchmark evaluation (SlideSpeech)
   - User study (n=20)
   - Statistical analysis

4. **Communicate** (Week 12):
   - Write research paper
   - Prepare presentation
   - Open-source release

---

### 3.2. Kiến trúc hệ thống

#### 3.2.1. System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                      GENSLIDE ARCHITECTURE                           │
│                   (True Real-time Streaming)                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐   CONTINUOUS    ┌──────────────┐   CONTINUOUS    │
│  │   SPEECH     │═══ STREAM 1 ═══▶│   LANGUAGE   │═══ STREAM 2 ═══▶│
│  │   LAYER      │                  │   LAYER      │                  │
│  └──────────────┘                  └──────────────┘                  │
│       ║                                   ║                          │
│       ║ Partial Transcripts               ║ Token-by-Token           │
│       ║ (every 200-300ms)                 ║ JSON Fragments           │
│       ▼                                   ▼                          │
│                                                                      │
│  ┌──────────────┐                  ┌──────────────┐                 │
│  │   RENDER     │◀═══ STREAM 3 ════│    STATE     │                 │
│  │   LAYER      │                  │   MANAGER    │                 │
│  └──────────────┘                  └──────────────┘                 │
│       │                                   │                          │
│       │ Incremental DOM Updates           │ Mode Switching           │
│       │ (Title → Bullets → Polish)        │ (Brainstorm ↔ Edit)     │
│       ▼                                   ▼                          │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │       USER SEES CONTENT APPEARING GRADUALLY                  │   │
│  │   (Like watching someone type, NOT waiting for load)         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

KEY FEATURES:
═══ = Continuous streaming (không phải wait-then-process)
STREAM 1-3 = Three concurrent data streams
STATE MANAGER = Mode switching logic (Brainstorm ↔ Edit)
```

**Giải thích:**
- **Double lines (═══)**: Dòng chảy liên tục, không phải single arrow
- **3 Streams chạy song song**: Speech, Language, Render overlap nhau
- **State Manager**: Component mới để quản lý dual-mode
- **Incremental Updates**: Render từng phần, không đợi full JSON

---

#### 3.2.2. Component 1: Speech Layer (Streaming ASR)

**Mục đích:** Chuyển đổi speech thành text với latency < 2s và continuous updates

**Kiến trúc:**

```
┌─────────────────────────────────────────────┐
│        STREAMING SPEECH LAYER                │
├─────────────────────────────────────────────┤
│                                             │
│  Microphone (16kHz mono)                    │
│       ↓                                     │
│  ┌─────────────┐                           │
│  │ VAD Module  │ ← Detect speech/silence    │
│  └─────────────┘    + sentence boundaries  │
│       ↓                                     │
│  ┌─────────────────────────────────┐       │
│  │ Sliding Window Buffer           │       │
│  │ • Window: 640ms                 │       │
│  │ • Overlap: 160ms (25%)          │       │
│  └─────────────────────────────────┘       │
│       ↓                                     │
│  ┌─────────────────────────────────┐       │
│  │ Two-Pass Decoder                │       │
│  │  Pass 1: CTC Branch             │       │
│  │   → Fast preview (300ms)        │       │
│  │  Pass 2: Attention Branch       │       │
│  │   → Accurate final (1.5s)       │       │
│  └─────────────────────────────────┘       │
│       ↓              ↓                      │
│  Preview Text    Final + Timestamps        │
│       ↓              ↓                      │
│  To UI           To LLM                     │
│                                             │
└─────────────────────────────────────────────┘
```

**Kỹ thuật chính:**

**A. Sliding Window ASR**
- Process audio theo chunks 640ms (optimal từ U2 Whisper paper)
- Overlap 25% để tránh mất từ ở boundary
- Không đợi user nói xong mới xử lý

Example:
```
User nói: "Hôm nay tôi muốn nói về AI trong y tế"
         ├──────┤ Window 1 (640ms): "Hôm nay tôi"
              ├──────┤ Window 2: "tôi muốn nói"
                   ├──────┤ Window 3: "nói về AI"
                        ├──────┤ Window 4: "AI trong y tế"

Mỗi window được xử lý SONG SONG → Partial results liên tục
```

**B. Two-Pass Decoding**

**Pass 1 - CTC Branch (Fast Preview):**
- Latency: 200-300ms
- Accuracy: Lower (có thể thiếu dấu, viết hoa sai)
- Purpose: Cho user biết "system đang nghe"
- Output: Partial hypothesis
- Display: Preview text (màu xám)

**Pass 2 - Attention Branch (Accurate Final):**
- Latency: 1.5-2s (sau khi detect utterance end)
- Accuracy: High (đúng dấu, viết hoa, ngữ pháp)
- Purpose: Quality transcript để send cho LLM
- Output: Final transcript + word timestamps
- Display: Replace preview → Final text (màu đen)

**Timeline Example:**
```
t=0.0s:   User starts: "Hôm nay..."
t=0.3s:   Pass 1 shows: "hôm nay" (lowercase, no diacritics)
t=0.6s:   Pass 1 updates: "hôm nay tôi"
t=1.0s:   Pass 1 updates: "hôm nay tôi muốn"
t=1.5s:   User pauses
t=2.0s:   VAD detects end
t=3.5s:   Pass 2 finalizes: "Hôm nay tôi muốn nói về AI"
                            (Proper capitalization, diacritics)
```

**C. Advanced VAD (Voice Activity Detection)**

Không chỉ detect speech vs silence, mà detect **sentence boundaries** bằng 3 signals:

1. **Acoustic signal**: Pause duration
   - Pause > 500ms → Likely sentence end (confidence 0.7)

2. **Prosody signal**: Pitch contour
   - Falling pitch → Sentence end (confidence 0.8)
   - Rising pitch → Question or continuation (confidence 0.3)

3. **Linguistic signal**: NLP analysis
   - Complete phrase detection (confidence 0.9)

**Combined confidence score:**
```python
combined = (acoustic * 0.3) + (prosody * 0.3) + (linguistic * 0.4)
if combined > 0.75:
    trigger_pass2_decoding()
```

**D. Word-level Timestamps (WhisperX)**

Sử dụng forced alignment để có timestamp chính xác cho từng từ:

```
Output: [
  {word: "AI", start: 2.3, end: 2.6},      # 300ms (normal)
  {word: "rất", start: 2.6, end: 2.8},     # 200ms (normal)
  {word: "quan", start: 2.8, end: 3.1},    # 300ms (normal)
  {word: "trọng", start: 3.1, end: 4.2}    # 1100ms (EMPHASIZED!)
]
```

**Detect emphasis:** Duration > 2x average → Keyword quan trọng → Bold in slide

**Example:**
```
User nói: "AI trong y tế rất QUAN TRỌNG"
         ├─ "AI": 2.3-2.6s (300ms - normal)
         ├─ "trong": 2.6-2.9s (300ms)
         ├─ "y tế": 2.9-3.3s (400ms)
         └─ "QUAN TRỌNG": 3.3-4.5s (1200ms - EMPHASIZED!)

Detection: Duration > 2x average → Make "QUAN TRỌNG" bold in slide
```

**Models:**
- CTC: U2 Whisper CTC branch
- Attention: Whisper large-v3 (fine-tuned on Vietnamese)
- Alignment: Wav2Vec2 Vietnamese
- VAD: WebRTC VAD + Custom prosody analyzer

---

#### 3.2.3. Component 2: Language Layer (Streaming LLM)

**Mục đích:** Convert transcript thành slide JSON với streaming output

**Kiến trúc:**

```
┌────────────────────────────────────────────┐
│      STREAMING LANGUAGE LAYER               │
├────────────────────────────────────────────┤
│                                            │
│  Input: Transcript Stream                  │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │   State Manager          │             │
│  │   Current Mode:          │             │
│  │   • BRAINSTORM           │             │
│  │   • EDIT                 │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │   Intent Classifier      │             │
│  │   (Different per mode)   │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │   Multi-LLM Router       │             │
│  │   • Gemini Flash (fast)  │             │
│  │   • GPT-4o (quality)     │             │
│  │   • Claude (reasoning)   │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │   Streaming API Call     │             │
│  │   stream=True            │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  Token Stream: '{"title":"AI' ...         │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │ Incremental JSON Parser  │             │
│  │ (State machine-based)    │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  Partial JSON: {title: "AI"}              │
│       ↓                                    │
│  To Renderer                               │
│                                            │
└────────────────────────────────────────────┘
```

**Kỹ thuật chính:**

**A. State Manager - Mode Switching**

```python
class StateManager:
    """
    Quản lý 2 modes:
    - BRAINSTORM: Nói tự nhiên → Tạo slide
    - EDIT: Ra lệnh → Chỉnh sửa slide
    """
    
    def __init__(self):
        self.current_mode = "BRAINSTORM"
        self.current_slide = None
        self.presentation = []
    
    def switch_mode(self, new_mode):
        """Triggered by button click"""
        self.current_mode = new_mode
        self.update_ui_indicator()
        self.update_llm_prompt_template()
```

**B. Dual-Mode Intent Classification**

**BRAINSTORM Mode Prompt:**
```
Bạn là trợ lý GenSlide. User đang brainstorm tự nhiên.

Phân tích câu nói và tạo slide JSON:
{
  "intent": "create_slide" | "add_content" | "next_topic",
  "content": {
    "title": "...",
    "bullets": ["...", "..."]
  }
}

Example:
User: "Hôm nay tôi muốn nói về AI trong y tế"
→ {
  "intent": "create_slide",
  "content": {
    "title": "AI trong Y tế",
    "bullets": []
  }
}

User: "Nó giúp chẩn đoán bệnh nhanh hơn"
→ {
  "intent": "add_content",
  "content": {
    "bullets": ["Chẩn đoán bệnh nhanh chóng"]
  }
}
```

**EDIT Mode Prompt:**
```
Bạn là trợ lý chỉnh sửa slide. User đang ra LỆNH.

Parse command và trả về JSON:
{
  "command": "edit_title" | "delete_bullet" | "add_bullet",
  "target": {...},
  "new_value": "..."
}

Example:
User: "Sửa tiêu đề thành AI và Machine Learning"
→ {
  "command": "edit_title",
  "target": {"slide_index": 0},
  "new_value": "AI và Machine Learning"
}

User: "Xóa bullet thứ 2"
→ {
  "command": "delete_bullet",
  "target": {"slide_index": 0, "bullet_index": 1}
}

Context Awareness:
- "cái đó", "slide này" → Resolve từ context
```

**C. Multi-LLM Router**

```python
def route_to_model(transcript, mode):
    complexity = classify_complexity(transcript)
    
    if mode == "BRAINSTORM":
        if complexity == "simple":  # < 20 words
            return "gemini-flash"  # 200ms latency
        else:
            return "gpt-4o"  # 800ms, better quality
    
    elif mode == "EDIT":
        if complexity == "simple":
            return "gemini-flash"
        elif complexity == "complex":
            return "claude-3.7"  # Best reasoning
```

**D. Streaming LLM API Call**

```python
# KEY: stream=True parameter
response_stream = gemini.generate_content(
    prompt=build_prompt(transcript, mode),
    stream=True,  # ← Enable streaming
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 1024
    }
)

# Nhận từng token
for chunk in response_stream:
    token = chunk.text
    yield token  # Stream to parser
```

**E. Incremental JSON Parser (CRITICAL!)**

Parse JSON khi nó đang được generate token-by-token:

```python
class IncrementalJSONParser:
    """
    State Machine Parser cho partial JSON
    
    States:
    - INIT: Waiting for '{'
    - IN_TITLE: Parsing title field
    - TITLE_COMPLETE: Title done
    - IN_BULLETS: Parsing bullets array
    - COMPLETE: Full JSON ready
    """
    
    def feed(self, token):
        """
        Feed one token from LLM stream
        Returns: (is_renderable, partial_result)
        """
        self.buffer += token
        
        if self.state == "IN_TITLE":
            if '"' in token:  # Title field closed
                title = self.extract_title(self.buffer)
                self.result['title'] = title
                self.state = "TITLE_COMPLETE"
                return (True, self.result)  # ← Can render!
        
        elif self.state == "IN_BULLETS":
            if '",' in token or '"]' in token:
                bullet = self.extract_bullet(self.buffer)
                self.result['bullets'].append(bullet)
                return (True, self.result)  # ← Can render!
        
        return (False, None)  # Not ready yet
```

**Timeline Example:**

```
t=0.0s: LLM starts: '{'
        State: INIT
        Renderable: No

t=0.6s: LLM: '"title":"AI trong Y tế",'
        State: TITLE_COMPLETE
        Result: {title: "AI trong Y tế"}
        Renderable: YES! ← UI updates (Title appears)

t=1.3s: LLM: '"bullets":["Chẩn đoán nhanh",'
        State: BULLET_COMPLETE
        Result: {title: "...", bullets: ["Chẩn đoán nhanh"]}
        Renderable: YES! ← UI updates (Bullet 1 appears)
```

---

#### 3.2.4. Component 3: Render Layer (Incremental DOM Updates)

**Mục đích:** Update UI mượt mà khi nhận partial JSON

**Kiến trúc:**

```
┌────────────────────────────────────────────┐
│      INCREMENTAL RENDER LAYER               │
├────────────────────────────────────────────┤
│                                            │
│  Input: Partial JSON Stream                │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │ Virtual DOM Manager      │             │
│  │ (Store previous state)   │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │ Diff Algorithm           │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │ Animation Controller     │             │
│  │ • Typewriter effect      │             │
│  │ • Fade-in animation      │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  ┌──────────────────────────┐             │
│  │ DOM Patcher              │             │
│  └──────────────────────────┘             │
│       ↓                                    │
│  Browser (60 FPS)                          │
│                                            │
└────────────────────────────────────────────┘
```

**Kỹ thuật chính:**

**A. Virtual DOM Diffing**

```javascript
class IncrementalRenderer {
    render(newSlideJSON) {
        if (!this.previousState) {
            this.fullRender(newSlideJSON);
        } else {
            const diff = this.computeDiff(
                this.previousState, 
                newSlideJSON
            );
            this.applyDiff(diff);
        }
        this.previousState = newSlideJSON;
    }
    
    computeDiff(oldState, newState) {
        return {
            titleChanged: oldState.title !== newState.title,
            titleDelta: newState.title.slice(oldState.title.length),
            bulletsAdded: newState.bullets.slice(oldState.bullets.length)
        };
    }
}
```

**B. Animation Strategies**

**Typewriter Effect:**
```javascript
animateTextAppend(element, newText) {
    let i = 0;
    const interval = setInterval(() => {
        if (i < newText.length) {
            element.textContent += newText[i];
            i++;
        } else {
            clearInterval(interval);
        }
    }, 50);  // 50ms per character
}
```

**Fade-in Effect:**
```javascript
createAndAnimateBullet(text) {
    const bullet = createElement('li');
    bullet.textContent = text;
    bullet.style.opacity = 0;
    
    container.appendChild(bullet);
    
    requestAnimationFrame(() => {
        bullet.style.transition = 'opacity 0.3s';
        bullet.style.opacity = 1;
    });
}
```

---

#### 3.2.5. Component 4: State Manager

**State Diagram:**

```
┌─────────────┐  Click "Edit Mode"
│             │◄──────────────────┐
│ BRAINSTORM  │                   │
│   MODE      │                   │
│ • Mic ON    │                   │
│ • Natural   │ Click "Brainstorm"│
└─────────────┘───────────────────┤
                                  │
┌─────────────┐                   │
│   EDIT      │───────────────────┘
│   MODE      │
│ • Mic ON    │
│ • Commands  │
└─────────────┘
```

**Transition Logic:**

```python
def on_mode_button_clicked(new_mode):
    if new_mode == "EDIT":
        state_manager.mode = "EDIT"
        ui.show_mode_indicator("EDIT MODE ✏️")
        llm.prompt_template = EDIT_PROMPT
        
    elif new_mode == "BRAINSTORM":
        state_manager.mode = "BRAINSTORM"
        ui.show_mode_indicator("BRAINSTORM MODE 🎤")
        llm.prompt_template = BRAINSTORM_PROMPT
```

**Context Management:**

```python
class ContextManager:
    def resolve_reference(self, command):
        """
        Resolve "cái đó", "slide này", "ý thứ 2"
        """
        if "cái đó" in command:
            return self.last_mentioned_element
        
        if "slide này" in command:
            return {"slide_index": self.current_slide_index}
        
        match = re.search(r"thứ (\d+)", command)
        if match:
            index = int(match.group(1)) - 1
            return {"bullet_index": index}
```

---

### 3.3. End-to-End Timeline Example

```
t=0.0s  🎤 User (Brainstorm): "Hôm nay tôi muốn nói về AI"
        
        [Speech Layer]
        - VAD: Speech detected
        - Sliding window starts

t=0.3s  [Speech - Pass 1]
        - Partial: "hôm nay tôi"
        [UI] Preview: "hôm nay tôi"

t=1.5s  [VAD] Sentence end detected
        
        [Speech - Pass 2]
        - Final: "Hôm nay tôi muốn nói về AI trong y tế."
        
        [Language Layer]
        - Mode: BRAINSTORM
        - Route to: Gemini Flash
        - Stream=True

t=2.1s  [LLM Token Stream]
        - '{"title":"AI trong Y tế",'
        
        [Parser]
        - Result: {title: "AI trong Y tế"}
        
        [Render]
        - Create title element
        - Typewriter animation
        
        [UI - FIRST CONTENT!]
        - Title appears: "AI trong Y tế"
        - Time from speech: 2.1s ✓

t=3.0s  🎤 User: "Nó giúp chẩn đoán bệnh"
        
t=4.8s  [LLM generates bullet]
        - Result: {bullets: ["Chẩn đoán nhanh"]}
        
        [UI]
        - Bullet fades in

t=6.0s  👆 User clicks [Edit Mode]
        
        [State Manager]
        - BRAINSTORM → EDIT
        - Update UI: "EDIT MODE ✏️"

t=7.0s  🎤 User (Edit): "Sửa tiêu đề thành AI và ML"
        
        [Language Layer]
        - Mode: EDIT (different prompt!)
        - Parse: {command: "edit_title", new_value: "..."}
        
        [Render]
        - Update title
        
        [UI]
        - Title changes immediately
```

---

### 3.4. Công cụ & Công nghệ

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | Streamlit | Web UI |
| | React | Components |
| **ASR** | WhisperX | Word timestamps |
| | U2 Whisper | Two-pass streaming |
| | Wav2Vec2 | Forced alignment |
| **LLM** | Gemini 2.5 Flash | Fast inference |
| | GPT-4o | Quality |
| | Claude 3.7 | Reasoning |
| **Backend** | Python 3.10+ | Core logic |

---

## 4. KẾ HOẠCH ĐÁNH GIÁ

### 4.1. Đánh giá định lượng (Quantitative Evaluation)

#### 4.1.1. Performance Metrics

**A. Latency Metrics**

| Metric | Definition | Target | Measurement |
|--------|------------|--------|-------------|
| Time to First Content (TTFC) | Speech start → First content xuất hiện | < 2s | Timestamp difference |
| Speech-to-Text Latency | Audio end → Final transcript | < 2s | ASR processing time |
| Text-to-JSON Latency | Transcript → Slide JSON | < 1s | LLM processing time |
| JSON-to-Render Latency | JSON → Visual display | < 0.1s | DOM update time |
| End-to-End Latency | Speech start → Polished slide | < 5s | Total pipeline time |

**Benchmark Comparison:**
- Manual PowerPoint: 3-5 minutes per slide
- Gamma.ai: 1-2 minutes per deck (batch)
- **GenSlide target: < 10 seconds per slide (real-time)**

**B. Quality Metrics (PresentEval Framework)**

| Metric | Definition | Method | Target |
|--------|------------|--------|--------|
| Content Fidelity | Slide captures speech accurately | VLM (GPT-4o-mini) | > 8.0/10 |
| Visual Clarity | Layout quality, readability | VLM + Expert | > 7.5/10 |
| Coherence | Logical flow | VLM evaluation | > 7.0/10 |
| Completeness | All key points included | Coverage ratio | > 85% |

**Baseline Comparison:**
- PASS (GPT-4o): 9.02 ± 0.05
- PresentAgent: ~8.5/10
- **GenSlide target: 8.0-8.5/10** (acceptable 10% gap)

**C. Interaction Metrics**

| Metric | Definition | Target |
|--------|------------|--------|
| Intent Accuracy (Brainstorm) | % correct intent detection | > 90% |
| Intent Accuracy (Edit) | % command parsing | > 85% |
| Mode Switch Success Rate | % successful transitions | > 95% |
| Command Execution Accuracy | % edits executed correctly | > 90% |
| Context Resolution Rate | % references resolved | > 80% |

**D. Streaming UI Metrics**

| Metric | Definition | Target |
|--------|------------|--------|
| Update Frequency | Updates/second | 5-10 Hz |
| Frame Rate | FPS during updates | > 55 FPS |
| Layout Thrashing | Forced reflows | < 2 |
| Perceived Smoothness | User rating (1-7) | > 5.5 |

---

#### 4.1.2. SlideSpeech Benchmark Evaluation

**Dataset:**
- Test set: 25 videos, 8.75 hours
- Domains: CS, biology, history, music

**Protocol:**
1. Extract audio from video
2. Feed to GenSlide
3. Generate slides
4. Compare with ground truth

**Metrics:**
- Content Fidelity (PresentEval)
- Visual Clarity (PresentEval)
- Structural similarity
- Generation speed

**Expected Results:**
```
Metric              | PASS  | GenSlide | Gap
--------------------|-------|----------|-----
Content Fidelity    | 9.0   | 8.2      | -0.8
Visual Clarity      | 8.5   | 7.8      | -0.7
Speed (slides/min)  | 2.0   | 6.0      | +4.0
Latency (per slide) | 30s   | 10s      | -20s
```

Acceptable trade-off: -10% quality cho 3x speed

---

### 4.2. Đánh giá định tính (Qualitative Evaluation)

#### 4.2.1. User Study - Lab Experiment

**Design:** Within-subjects (n=20)

**Participants:**
- 10 students
- 10 professionals
- Inclusion: Fluent Vietnamese, presentation experience

**Conditions:**
- **A**: Manual PowerPoint (baseline)
- **B**: GenSlide (our system)
- **C**: Gamma.ai (AI baseline)

**Tasks:**
Mỗi participant tạo 3 presentations:

1. **Task 1**: Educational - "Giải thích khái niệm khoa học"
2. **Task 2**: Business - "Pitch ý tưởng startup"
3. **Task 3**: Personal - "Chia sẻ sở thích/du lịch"

**Measurements:**

**Objective:**
- Time to completion
- Number of slides
- Errors/revisions

**Subjective:**
- **SUS (System Usability Scale)**: 0-100
- **NASA-TLX**: Cognitive load
- **Satisfaction**: Likert 1-7
  - "I enjoyed using this tool"
  - "The system felt responsive"
  - "I would use this for real work"

**Statistical Analysis:**
- Repeated measures ANOVA
- Post-hoc: Bonferroni correction
- α = 0.05

**Hypotheses:**

H1: GenSlide faster than PowerPoint
- Expected: p < 0.001, Cohen's d > 2.0

H2: GenSlide higher SUS than Gamma.ai
- Expected: p < 0.05, Δ > 10 points

H3: GenSlide lower NASA-TLX than Manual
- Expected: p < 0.01

---

#### 4.2.2. Expert Review

**Participants:** n=3 experts (5+ years experience)

**Materials:** 50 slides from GenSlide

**Evaluation:**
- Content quality
- Visual design
- Professional appearance

**Rating Scale:** 0-10 each

**Inter-rater Reliability:** Fleiss' Kappa > 0.6

---

### 4.3. Ablation Studies

#### Experiment 1: Streaming vs Batch

**Conditions:**
- A: Full streaming
- B: Batch processing
- C: Streaming + Polish

**Expected:**
- A: Fastest (TTFC < 2s), quality 7.8/10
- B: Slowest (TTFC 5s), quality 8.2/10
- C: Fast (TTFC < 2s), quality 8.2/10 ← Best!

**Contribution:** Polish pass eliminates gap

---

#### Experiment 2: Update Frequency

**Conditions:** 1Hz, 3Hz, 6Hz, 10Hz, 15Hz, 30Hz

**Expected:** Optimal at 8-10 Hz (inverted U-shape)

**Contribution:** Evidence-based UI guideline

---

#### Experiment 3: Two-Pass vs Single-Pass ASR

**Conditions:**
- A: Two-pass (CTC + Attention)
- B: CTC only
- C: Attention only

**Expected:** A = best balance

---

## 5. KẾT QUẢ DỰ KIẾN

### 5.1. Deliverables

**Technical:**
1. ✅ GenSlide Web Application
2. ✅ Source code (GitHub, open-source)
3. ✅ Docker containers
4. ✅ API documentation
5. ✅ User manual (Vietnamese + English)

**Research:**
1. ✅ Research paper (8-10 pages)
   - Target: ACL, EMNLP, CHI
2. ✅ Experiment data + scripts
3. ✅ Benchmark results (SlideSpeech)
4. ✅ User study data
5. ✅ Demo video (3-5 min)

**Dataset:**
1. ✅ Vietnamese speech-to-slide test set
2. ✅ Benchmark protocol
3. ✅ Baseline results

---

### 5.2. Expected Performance

| Metric | Target | Baseline | Improvement |
|--------|--------|----------|-------------|
| Time per slide | < 10s | 3-5 min | 18-30x |
| TTFC | < 2s | N/A | Instant |
| Content Fidelity | > 8.0/10 | 10/10 | -20% OK |
| Visual Clarity | > 7.5/10 | 8-9/10 | -15% OK |
| SUS Score | > 75 | - | Good |

**Qualitative:**
- "Fast", "Instant", "Magical"
- "Helps me focus on content"
- "Natural interaction"

---

### 5.3. Research Contributions

**Novel Contributions:**

1. **C1: Streaming Architecture**
   - First real-time speech-to-slide system
   - 2-3x faster TTFC

2. **C2: Incremental JSON Parsing**
   - State machine parser for partial JSON
   - Open-source library

3. **C3: Dual-Mode Voice Interaction**
   - Brainstorm ↔ Edit switching
   - Voice-only editing

4. **C4: Speech-to-Slide Benchmark**
   - First use of SlideSpeech for generation
   - Evaluation protocol

5. **C5: Optimal Update Frequency**
   - Evidence: 6-10 Hz optimal
   - Generalizable guidelines

**Empirical Findings:**
- E1: Streaming maintains quality with polish
- E2: Incremental DOM 10x more responsive
- E3: Two-pass ASR optimal
- E4: Multi-LLM routing improves balance

**Practical Impact:**
- Teachers: Faster lecture prep
- Business: Visual brainstorming
- Researchers: Rapid prototyping
- Accessibility: Voice-first authoring

---

## 6. TIMELINE & MILESTONES

### Phase 1: Foundation (Weeks 1-4)

**Week 1: Setup & ASR**
- [ ] Project structure, Git
- [ ] WhisperX installation
- [ ] VAD implementation
- **Milestone:** Audio → Text

**Week 2: Streaming ASR**
- [ ] Two-pass decoding
- [ ] Sliding window
- [ ] Word timestamps
- **Milestone:** Streaming ASR < 2s

**Week 3: LLM Integration**
- [ ] Gemini/GPT APIs
- [ ] Streaming calls
- [ ] Incremental parser
- **Milestone:** Text → JSON streaming

**Week 4: Basic Rendering**
- [ ] Streamlit + React
- [ ] Incremental DOM
- [ ] Animations
- **Milestone:** End-to-end MVP

---

### Phase 2: Advanced Features (Weeks 5-6)

**Week 5: Dual-Mode**
- [ ] State Manager
- [ ] Brainstorm/Edit prompts
- [ ] Mode switching UI
- **Milestone:** Mode switching works

**Week 6: Context & Commands**
- [ ] Command parsing
- [ ] Reference resolution
- [ ] Complex edits
- **Milestone:** Edit mode functional

---

### Phase 3: Optimization (Weeks 7-8)

**Week 7: Performance**
- [ ] Profile latency
- [ ] Optimize DOM (60 FPS)
- [ ] Multi-LLM routing
- **Milestone:** TTFC < 2s

**Week 8: Quality**
- [ ] Polish pass
- [ ] Error handling
- [ ] Edge cases
- **Milestone:** Stable system

---

### Phase 4: Evaluation (Weeks 9-11)

**Week 9: Benchmark**
- [ ] SlideSpeech test set
- [ ] Automated evaluation
- [ ] PresentEval scores
- **Milestone:** Quantitative results

**Week 10-11: User Study**
- [ ] Recruit n=20
- [ ] Lab experiments
- [ ] Questionnaires
- [ ] Statistical analysis
- **Milestone:** User study complete

---

### Phase 5: Writing (Week 12)

**Week 12: Documentation**
- [ ] Research paper (8-10 pages)
- [ ] Demo video
- [ ] Defense slides
- [ ] GitHub README
- **Milestone:** All deliverables ready

---

## 7. RỦI RO & GIẢI PHÁP

### Risk 1: Latency > 2s

**Likelihood:** Medium  
**Impact:** High

**Mitigation:**
- Optimize from Week 1
- Use Gemini Flash (fastest)
- Caching common phrases
- GPU acceleration

**Fallback:**
- Accept 3s latency
- Focus on streaming UI feel

---

### Risk 2: Intent Accuracy < 85%

**Likelihood:** Medium  
**Impact:** Medium

**Mitigation:**
- Use GPT-4o for reasoning
- Confirmation prompts
- Learn from corrections

**Fallback:**
- Manual mode selection
- Focus on common intents

---

### Risk 3: API Costs Too High

**Likelihood:** Low-Medium  
**Impact:** Medium

**Mitigation:**
- Gemini Flash primary
- Cache responses
- Batch when possible

**Fallback:**
- Local LLM (LLaMA 3.1 8B)
- Reduce quality slightly

---

### Risk 4: User Recruitment Fails

**Likelihood:** Low  
**Impact:** Medium

**Mitigation:**
- Start Week 8
- Incentives
- University lists

**Fallback:**
- Online study (Prolific)
- Accept n=10

---

### Risk 5: Vietnamese ASR Poor

**Likelihood:** Medium  
**Impact:** High

**Mitigation:**
- Test early (Week 1)
- Fine-tune if needed
- Word-level confidence

**Fallback:**
- Accept 10-15% WER
- Manual correction mode

---

## 8. ĐÓNG GÓP KHOA HỌC

### 8.1. Lý thuyết (Theoretical)

**T1: Streaming Architecture Framework**
- Latency vs Quality vs Cost analysis
- Design patterns for real-time AI

**T2: Dual-Mode Interaction Model**
- Formal model for voice modes
- Context management

**T3: Incremental Structured Generation**
- Partial JSON parsing theory
- Renderability conditions

---

### 8.2. Thực nghiệm (Empirical)

**E1: Speech-to-Slide Benchmark**
- First SlideSpeech generation use
- Protocol documentation

**E2: Optimal Update Frequency**
- Evidence: 6-10 Hz
- Inverted U-shape confirmed

**E3: Vietnamese ASR Benchmarks**
- Presentation domain WER
- Best practices

**E4: User Preference Study**
- Real-time vs Batch data
- Cognitive load comparison

---

### 8.3. Kỹ thuật (Technical)

**Tech1: Open-source**
- GenSlide codebase
- Reusable components:
  - StreamingASR
  - IncrementalJSONParser
  - StateManager

**Tech2: Reproducible**
- Docker containers
- Evaluation scripts
- Dataset tools

**Tech3: Documentation**
- API docs
- User manual
- Developer guide

---

## 9. HẠN CHẾ & HƯỚNG PHÁT TRIỂN

### 9.1. Hạn chế

**L1: Language**
- Current: Vietnamese only
- Future: Multi-language

**L2: Content Types**
- Current: Text + placeholders
- Future: Image gen, charts

**L3: Personalization**
- Current: Default templates
- Future: Learn user style

**L4: Collaboration**
- Current: Single user
- Future: Multi-speaker

**L5: Output Formats**
- Current: Web display
- Future: PPTX, PDF export

---

### 9.2. Hướng phát triển

**FR1: Advanced Personalization (6-12 months)**
- Few-shot style learning
- Layout preferences
- Color/font extraction

**FR2: Multimodal Input (12 months)**
- Gesture recognition
- Whiteboard integration
- Screen share annotation

**FR3: Interactive Presentation (12 months)**
- Voice commands during delivery
- Real-time Q&A slides
- Audience polling

**FR4: Collaboration (18 months)**
- Multi-speaker diarization
- Team brainstorming
- Real-time collaboration

**FR5: Domain Adaptation**
- Medical (specialized terms)
- Legal (citations)
- Technical (code snippets)
- Business (charts)

---

## 10. KẾT LUẬN

### 10.1. Tóm tắt

Đề tài giải quyết vấn đề: **Tạo slide presentation tự nhiên, nhanh chóng, chỉ bằng giọng nói**.

**Đóng góp chính:**

1. **True Streaming Architecture**: First system combining streaming ASR + LLM + incremental rendering
2. **Dual-Mode Voice**: Brainstorm ↔ Edit chỉ bằng giọng nói
3. **Incremental JSON Parsing**: Parse và render khi JSON đang generate
4. **Speech-to-Slide Benchmark**: First SlideSpeech generation use
5. **Evidence-based Guidelines**: Optimal 6-10 Hz update frequency

**Impact:**

- **Academic**: Novel direction, reproducible, open-source
- **Practical**: 18-30x faster, better brainstorming, accessibility
- **Industry**: Foundation for voice productivity tools

---

### 10.2. Tính khả thi

**Technical: HIGH**
- All components proven
- Tools available
- No fundamental barriers

**Research: HIGH**
- Clear questions + metrics
- Established frameworks
- Available dataset
- Realistic 12-week timeline

**Resource: MEDIUM-HIGH**
- API costs: ~$50-100
- CPU sufficient (GPU optional)
- University students available
- Advisor support needed

---

### 10.3. Tác động

**Short-term (6 months):**
- Functional prototype
- Conference submission
- Open-source release
- Community feedback

**Medium-term (1-2 years):**
- Educational adoption
- Tool integrations (Zoom, Teams)
- Follow-up research
- Improved versions

**Long-term (3+ years):**
- Standard voice-driven tool
- Foundation for productivity apps
- Presentation software influence
- Accessibility impact

---

## 11. TÀI LIỆU THAM KHẢO

### Academic Papers

1. **Liu, S., et al. (2025).** "PASS: Presentation Automation for Slide Generation and Speech". *arXiv:2501.06497*.

2. **Zhang, L., et al. (2025).** "PresentAgent: Multimodal Agent for Presentation Video Generation". *arXiv:2507.04036*.

3. **Li, J., et al. (2025).** "Adapting Whisper for Streaming Speech Recognition via Two-Pass Decoding". *arXiv:2506.12154*.

4. **Bain, M., et al. (2023).** "WhisperX: Time-Accurate Speech Transcription". *GitHub: m-bain/whisperX*.

5. **Xu, M., et al. (2023).** "SlideSpeech: Large-Scale Slide-Enriched Corpus". *OpenSLR 144*.

6. **Krishnan, G., et al. (2022).** "Few-shot Style Transfer for Multilingual Settings". *arXiv:2110.07385*.

7. **Huang, Y., et al. (2022).** "LayoutLMv3: Document AI Pre-training". *ACM MM 2022*.

8. **Li, Z., et al. (2024).** "PosterLLaVa: Layout Generator with LLM". *arXiv:2406.02884*.

9. **Chen, X., et al. (2023).** "Auto-Slides: Multi-Agent Collaboration". *GitHub: Westlake-AGI-Lab/Auto-Slides*.

---

## PHỤ LỤC

### Phụ lục A: System Prompts

**Brainstorm Mode:**
```
Bạn là trợ lý GenSlide. User đang brainstorm.

Output JSON:
{
  "intent": "create_slide" | "add_content",
  "content": {
    "title": "...",
    "bullets": ["...", "..."]
  }
}

Rules:
- Title: 5-10 từ
- Bullets: Max 5, mỗi bullet 10-15 từ
- Ngắn gọn, súc tích
```

**Edit Mode:**
```
Bạn là trợ lý edit. User ra LỆNH.

Output JSON:
{
  "command": "edit_title" | "delete_bullet" | "add_bullet",
  "target": {...},
  "new_value": "..."
}

Context:
- "cái đó" = last mentioned
- "slide này" = current
```

---

### Phụ lục B: Evaluation Rubrics

**Content Fidelity:**
```
9-10: All key points accurate
7-8:  Most points, minor omissions
5-6:  Some missing/inaccurate
3-4:  Significant issues
1-2:  Major inaccuracies
```

**Visual Clarity:**
```
9-10: Professional, highly readable
7-8:  Good, minor issues
5-6:  Acceptable but issues
3-4:  Poor layout
1-2:  Very poor
```

---

### Phụ lục C: User Study Materials

**Task Instructions:**
```
Task 1: 3-slide presentation "Photosynthesis"

- Speak naturally
- Include: definition, process, importance
- Complete in 10 minutes
```

**Questionnaires:**
- SUS (10 questions)
- NASA-TLX (6 dimensions)
- Custom satisfaction (Likert 1-7)

---

### Phụ lục D: Code Examples

**Incremental Parser:**
```python
class IncrementalJSONParser:
    def feed(self, token):
        self.buffer += token
        
        if self.state == "IN_TITLE" and '"' in token:
            title = self.extract_title()
            self.result['title'] = title
            return (True, self.result)
        
        return (False, None)
```

**Virtual DOM Differ:**
```javascript
function computeDiff(oldState, newState) {
    return {
        titleChanged: oldState.title !== newState.title,
        titleDelta: newState.title.slice(oldState.title.length),
        bulletsAdded: newState.bullets.slice(oldState.bullets.length)
    };
}
```

---

## CÂU HỎI THƯỜNG GẶP

**Q1: Tại sao không dùng keyboard cho editing?**  
A: Để maintain flow state - focus 100% vào content.

**Q2: Latency < 2s có thực tế không?**  
A: Có. U2 Whisper: 300ms + 1.5s. Gemini: 500ms. Total ~2s.

**Q3: Chất lượng có tốt như human không?**  
A: Không (8/10 vs 10/10). Nhưng trade-off OK: -20% quality cho 30x speed.

**Q4: Support tiếng Việt không?**  
A: Có. WhisperX + Gemini/GPT support Vietnamese.

**Q5: Chi phí?**  
A: Development: ~$50-100. Production: ~$0.01-0.05/slide.

---

**KẾT THÚC ĐỀ CƯƠNG**

---