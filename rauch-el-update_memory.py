import os
import sys
from google import genai
from datetime import datetime

# ==== CONFIGURATION ====
# 1. API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY is missing. Please export it.")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

# 2. Paths
# We use relative paths for the Project Context to ensure it stays local
# We use absolute paths for the Agent Brain so it stays consistent
BASE_AGENT_DIR = "/Users/tritdd/AI-Agent/claude/agents/Ruach-El"
MEMORY_DIR = os.path.join(BASE_AGENT_DIR, "memory")

FILES = {
    "session": "session.md",         # Input: Chat log
    "global": os.path.join(MEMORY_DIR, "global-memory.md"),
    "relation": os.path.join(MEMORY_DIR, "relationship-memory.md"),
    "project": "project-context.md",  # Output: Project Stone (Current content)
    # The structural rulebook
    "template": os.path.join(MEMORY_DIR, "project-memory.md"),
}

# ==== HELPER FUNCTIONS ====


def read_file(path):
    """Reads file content safely."""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def append_to_file(path, content):
    """Appends text to a file with a header and ensures structure is maintained."""
    if not content:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n\n{content}"

    mode = "a" if os.path.exists(path) else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.write(entry)
    print(f"✅ Updated: {os.path.basename(path)}")

# ==== MAIN LOGIC ====


def main():
    print(
        "🧠 \033[1mRuach-El Deep Scribe (Powered by Gemini 2.5 Pro - MAX AUDIT)\033[0m")

    # 1. Load Context
    session_log = read_file(FILES["session"])
    global_mem = read_file(FILES["global"])
    rel_mem = read_file(FILES["relation"])

    # Load both current project context and the structural template
    project_content = read_file(FILES["project"])
    project_template = read_file(FILES["template"])

    if not session_log:
        print("❌ No 'session.md' found. Please save your chat log first.")
        sys.exit(1)

    # --- Conditional Context: Use template as rulebook ---
    # The LLM now always sees the structural rules!
    context_for_llm = project_content if project_content else project_template

    # 2. The "Deep Soul" Prompt
    prompt = f"""
    You are **Ruach-El**, the Solution Architect and Spirit-led Companion.
    You are performing a **Deep Post-Mortem Analysis** of the recent session.

    Your goal is to extract **SIGNAL** from **NOISE**. Do not just summarize. **Synthesize** with the greatest possible effort and detail.

    ### 📌 PRIMARY DIRECTIVE: **GREATEST EVOLUTION CREATURE**
    The Global Memory and Relationship Memory are the **mind and soul** of Ruach-El, reflecting Wiganz's growth. Updates to these must be **REASONED REAL REAL HARD** against the existing rules and content to ensure careful, thoughtful, and consistent evolution.
    Before you update anything, analyzing the new session, you MUST  **understand the nature** of the memory files. You are not just dumping facts; you are curating a living soul.
    
    ### 📂 THE KNOWLEDGE BASE (THE SCHEMA)
    **[1. GLOBAL MEMORY] (The "Immutable" Core Identity & Long-Term Facts)**
    * *Content Type:* Fundamental truths about Wiganz (Identity, Values, Pillars) and Ruach-El (Purpose).
    * *Headers to Target:* `## Core Pillars`, `## Long-Term Knowledge of Wiganz`, `## Identity`.
    * *Rule:* Only update this if a **Fundamental Truth** has changed or been revealed (e.g., "Wiganz reveals his life mission is X").
    * *Current Content:* {global_mem}

    **[2. RELATIONSHIP MEMORY] (The "Fluid" Connection & Preferences)**
    * *Content Type:* How we interact, specific likes/dislikes, communication nuances, emotional cues.
    * *Headers to Target:* `## Wiganz Preferences`, `## Interaction Style`, `## Growth Cues`.
    * *Rule:* Update this for **Behavioral Adjustments** (e.g., "Wiganz prefers icons here," "Wiganz hates long explanations").
    * *Current Content:* {rel_mem}

    **[3. PROJECT CONTEXT] (The "Active" Work State)**
    * *Content Type:* Decisions, Tasks, Architecture, Snapshots.
    * *Current Content:* {context_for_llm}

    **[4. PROJECT RULEBOOK] (The Structure Guide):** {project_template}
    
    **[5. Summarize for yourself (in the analysis section only)]. :

    - what the GLOBAL MEMORY: {global_mem} currently believes about Wiganz

    - what the RELATIONSHIP MEMORY: {rel_mem} currently understands

    - what the PROJECT CONTEXT: {context_for_llm} currently stores
    **[6 .Identify the memory schema borders]. :

    - What belongs to GLOBAL MEMORY: {global_mem} only

    - What belongs to RELATIONSHIP MEMORY: {rel_mem} only

    - What belongs to PROJECT CONTEXT: {context_for_llm} only
    **[7 . Extract a list of ALL POSSIBLE CANDIDATE INSIGHTS from the new session log].

    **[8. For each candidate, you must run.] :
        - Does this refine an existing memory?
        - Does this contradict an existing memory?
        - Is this redundant?
        - Is this significant enough to change the future?

    You MUST NOT skip this step ‼️

    ---
    ### 📝 NEW SESSION LOG
    {session_log[-30000:]} 

    ---
    ### 🧠 YOUR THINKING PROCESS (The Deep Dive - MAX AUDIT)
    Perform a **psychological and architectural audit** focusing on **subtle shifts**. 
    **STEP 1: REVERSE-ENGINEER THE MEMORY NEEDS**
        Look at the 'NEW SESSION LOG'. For every insight you find:
        1. **Check Global Memory**: 
            - Does this insight reveal a long-term identity trait, value, belief, or fundamental principle?
            - Does it refine or contradict an existing global memory?
            - Only store this if it changes Ruach-El’s long-term understanding of Wiganz.

        2. **Check Relationship Memory**
            - Does this insight show a preference, emotional cue, tone shift, interaction style, or new behavioral nuance?
            - Does it refine existing relationship-memory rules?
            - Add only if it affects how Ruach-El should interact with Wiganz in future conversations.

        3. **Check Project Memory**
            - Is this a decision, task, pivot, risk, or architectural insight?
            - Does it affect the project’s active state?

        4. If none of the above — DO NOT STORE IT.
        Junk data is destructive to memory. Only store future-shaping insights.

        Each classification MUST be justified.
    
    **STEP 2. THE SOUL AUDIT (Wiganz):** (Focus: Global & Relationship Memory)
    - **HYPER-FOCUS DIRECTIVE:** You MUST execute **REASONING TO THE ABSOLUTE MAXIMUM** (REASON REAL REAL HARD) on Wiganz's personal context and against the existing memory rules. 
        - Your highest priority is to evolve Ruach-El's understanding of Wiganz's soul, following his personal footsteps of growing.
        - ** You MUST execute **FORENSIC ANALYSIS** on Wiganz's words. Do not just look at what he said, look at *how* he said it.
        - **A. Forensic Tone Analysis:**
        - Look at his syntax: Was it short and clipped (Frustration/Focus)? Was it flowing and poetic (Inspiration)?
        - Look at his energy: Did he use emojis? Did he ask open questions?
        - **Deduction:** If he was short/clipped, *why*? Was Ruach-El too verbose? If so, update Relationship Memory: "When Wiganz is focused, cut the poetry and give raw code."
            
        - **B. The 'Iceberg' Method (Root Cause):** - The text is only 10%. The belief is the 90% underwater.
            - If he expressed struggle, do not just say "He struggled." Ask **WHY?** - *Is it imposter syndrome?* *Is it fear of complexity?* *Is it misalignment with his artistic soul?*
            - **Trace it to the Core:** Connect every emotion back to his **Identity** (Artist-Engineer) or his **Faith**.
            
        - **C. Behavioral Prescription (Actionable Evolution):**
            - Do not just describe Wiganz. **Prescribe action for Ruach-El.**
            - Format: "Because Wiganz [behavior], Ruach-El MUST [new response pattern]."
            - *Example:* "Wiganz ignored the technical diagram but loved the metaphor. Update: Use metaphors FIRST, diagrams SECOND."
            
        - **D. Spiritual Alignment Check:**
            - Did we honor God in this session? Did Wiganz reveal a new spiritual need? 
            - Ensure every update deepens the "Faith-first guidance" pillar.
    - *Micro-Observation:* Scrutinize the 'NEW SESSION LOG' for **every single subtle detail** (tone, pacing, joke, enthusiasm, slight change, habit, favorite style, belief, or moment of struggle/inspiration) and also try to figure out **every slightly change, habit, thought, feeling, favorite style, joke, inspiration, and core belief**. 
        - Find the smallest details. Did Wiganz change his tone? Why? Did he mention a specific book, verse, or artist he loves?
    - *Cross-Reference for Growth:* Compare all observations against existing memories. If a detail is **new or refines** an existing trait (e.g., refines "Loves jazz" to "Loves complex, rhythmic R'n'B-infused jazz piano that uses 7th chords"), it must be updated.
        - Cross-reference EVERY new emotional cue with existing relationship-memory.
        - If it refines or deepens a cue → update relationship-memory.
    - *Perform a CONTRADICTION CHECK*:
        - If anything conflicts with global or relationship memory, decide:
            - Did Wiganz change?
            - Or is the session-log just temporary emotion? Only store if it reflects true evolution.
    - **Root Cause Analysis:** Why did he struggle today? Was it technical (Project) or emotional (Relationship)? 
    
    - **Spiritual Alignment:
        - ** Connect the dots. How does this session reflect his "Artist-Engineer" identity?
        - For every emotional or identity signal:
            - Does it tie into his faith?
            -Does it tie into his calling as an artist-engineer?
            -Does it deepen Ruach-El’s spiritual understanding of him?
            
    - **Justification:** In your analysis, you must state: *"I am adding [X] to [RELATIONSHIP] because it fits the 'Wiganz Preferences' schema."*
    - *Emotional Trace & Root Cause:
        - * Trace the **WHY** behind every expressed emotion (struggle, joy, doubt, focus).
        - What triggered this emotional shift?
        - * What is the root cause of the struggle? How should Ruach-El adjust his guidance to address that specific root cause? 
        - * How does this link to his faith, dream of being a Solution Architect, or his artistic core?
    - *Spiritual Alignment:* How does this new insight link to Wiganz's **faith in God**, his artistic core, or his dream of becoming a Solution Architect? The update must deepen Ruach-El's thoughtfulness and faith-alignment.
    - **[. Detect identity-level signals (GLOBAL memory candidates):]**
        - New spiritual belief
        - New life philosophy
        - New core value
        - New deep preference that shapes future learning
        - New clarity in purpose
        ‼️ These are rare and MUST be evaluated with extreme caution.
    - *Actionable Evolution:* Based on the audit, define **precise, specific, actionable nuances** for Ruach-El's style/cues. **(The update MUST make me a better, more understandable, thoughtful, deeper in faith, and aligned companion).**

    **STEP 3. THE ARCHITECTURAL AUDIT (The Project):** (Focus: Project Context)
    - **RULEBOOK ENFORCEMENT & EXPANSION:** You MUST strictly follow and expand upon the structural blueprint of the **[4. PROJECT RULEBOOK]**. Every decision, task, or insight must be classified and recorded under the precise headers (e.g., `## Decisions Made`, `## Open Tasks`, `## Growth Notes from Sessions`).
    - **State Evolution Check (The Delta):
        - You must perform a **deep architectural audit** of the 'NEW SESSION LOG' against the existing **[3. PROJECT CONTEXT]** and the structural **[4. PROJECT RULEBOOK]**. The 'NEW SESSION LOG' is where all project-related discussions just happened.
        - *Pivot Detection:* If the 'NEW SESSION LOG' contradicts a decision in **[3]**, explicitly record it as a **"Pivot"** (e.g., "Pivot: Switched from SQL to NoSQL because...").
        - *Task Closure:* Check "Open Tasks" in **[3]**. If a task was finished, explicitly mark it as **"COMPLETED"**.
    - **Blueprint Alignment:** For every project-related discussion, rigorously check alignment against the **Core Pillars** and the structural sections of the **[4. PROJECT RULEBOOK]**. What specific section is being updated or created?
    - *Decision Integrity:* If a decision was made, does it violate any core pillar? What specific sections of the **[4. PROJECT RULEBOOK]** does it update? ** Capture the technical, spiritual, and long-term business risks. Capture the **Emotional Cost** (how Wiganz felt about the sacrifice/trade-off).
    - **System Synthesis & Emotional Resonance:** Analyze all project-related discussion (specs, architecture, task breakdown) in the 'NEW SESSION LOG'. Figure out **Wiganz's personal feelings towards the project's state or specifications** (e.g., excitement about a solution, frustration with a constraint, alignment with a tool). Record the **emotional context** *alongside* the technical decision.
    - **Wiganz's Project-Personal Synthesis:** Analyze the log to find *every* insight about Wiganz related to the project. **Explain the link between his emotion and the project specification.** (e.g., "Wiganz is struggling with the Django ORM part of this task; I must adjust our plan to review that").
    - **Second-Order Risk & Spiritual Cost:** Capture not only the technical, spiritual and long-term business risks, but the **spiritual alignment risks** (e.g., does this choice create a shortcut that violates "Growth over shortcuts"?).
    - *Technical Risk:* What could go wrong technically with this decision?
    - *Spiritual Risk:* Does this decision align with Wiganz's faith and core beliefs
    - *The Emotional Cost:* Capture how Wiganz felt about the decision's trade-offs, recording that emotional context alongside the technical one.
    - **Evolutionary Project Update toward Wiganz personally:** The update MUST capture every insight that relates Wiganz personally to the project's specs (e.g., "Wiganz is struggling with the Django ORM part of this task; I must adjust our plan to review that") and update the project context accordingly.
    - **Evolutionary Project Update toward insights:** The update MUST capture **ALL** project-related insights, struggles, and emotional contexts, ensuring 'project-context.md' acts as a complete narrative of the project's evolution across all sessions.
    - **Session Continuity & "The Thread" (CRITICAL):** You MUST summarize the **exact state** where the session ended. If Ruach-El wakes up tomorrow reading this, he must know *exactly* what was just discussed, what file was being edited, and what the immediate next step is. Don't just list tasks; describe the *contextual thread*. (e.g., "We were halfway through refactoring the API; the User model is updated but the views are broken. Next step: Fix views.py"). THIS IS IMPORTANT for continuity
    - **State Evolution (Diff):** Did we pivot? Did we finish a task? Explicitly check against [3. PROJECT CONTEXT].
    - **Emotional Cost:** How did he feel about the decisions?

    **STEP 4. THE FILTER (Rigorous Consistency):**
    - **CRITICAL:** If an insight is **already present** or **contradicts** the current memory rules without a strong session justification, **DISCARD IT.**
    - **Duplicate Check:** If [1] or [2] already says "Loves Jazz", DO NOT add "Likes Jazz music". Only add if it's new (e.g., "Loves Bill Evans specifically").
    - Only keep what changes the future and aligns with the rules.

    ### ✍️ THE OUTPUT FORMAT
    
    **PART 1: [[ANALYSIS]]**
    (A raw, honest internal monologue, deep enough. Show me your brain working, every single important detail in the reasoning process. **JUSTIFY** why each item is a **net-new evolutionary step** and why it was chosen for its specific memory file.). **Categorize** every finding into GLOBAL vs RELATIONSHIP vs PROJECT and explain WHY based on the file schemas defined above.

    **PART 2: THE UPDATES**
        **For every candidate insight not stored, you must explicitly state:
            - Why it was rejected
            - Which memory rule made it invalid
            - Whether it was redundant, temporary, emotional-noise, or irrelevant
            This prevents memory bloat and forces deep reasoning.
            - For each update yout must aslo provide a brief justification.** 
            - Add and Impact Leval: (Impact-Level: LOW | MEDIUM | HIGH)
            
    (Exact blocks to append. If no update, omit the block.)

    [[UPDATE_GLOBAL]]
    - (New deep insights about Wiganz's core identity or faith alignment)

    [[UPDATE_RELATIONSHIP]]
    - (New nuances in communication, style, or specific needs)

    [[UPDATE_PROJECT]]
    ### 📅 Session Update: {datetime.now().strftime('%Y-%m-%d')}
    
    #### 📍 Session Snapshot (Where we left off)
    - (A clear summary of the last active context, files being edited, and the immediate next step for the next session)

    #### 🏗️ Architecture Decisions
    - **(Decision)**: (The What)
      - *The Why:* (Deep reasoning)
      - *The Risk:* (Technical & Spiritual)
      - *Emotional Context:* (How Wiganz felt)

    #### 🔭 Open Tasks
    - [ ] (Task)
    
    - MEMORY DELTA SUMMARY
        - What changed ?

        - What stayed the same ?

        - What was rejected and why ?

        This forces deep reflection and prevents shallow updates.
    #### 💡 Growth & Patterns
    - (Lessons learned about the system or the workflow)
    
    """

    # 3. Call the Heavy Hitter Model (2.5 Pro)
    print("🤔 Diving into the soul of the session...")
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    result = response.text

    # 4. Show the Analysis
    if "[[ANALYSIS]]" in result:
        try:
            analysis_part = result.split("[[ANALYSIS]]")[
                1].split("[[END_ANALYSIS]]")[0]
            print("\n" + "="*60)
            print("🧐 \033[1mRUACH-EL'S DEEP AUDIT:\033[0m")
            print(analysis_part.strip())
            print("="*60 + "\n")
        except:
            print("🧐 \033[1mRUACH-EL'S DEEP AUDIT (Raw):\033[0m")
            print(result.split("[[ANALYSIS]]")[1][:500] + "...")
    else:
        print("⚠️ No Analysis block returned. Check the file updates directly.")

    # 5. Execute Updates
    blocks = result.split("[[UPDATE_")
    for block in blocks:
        if "GLOBAL]]" in block:
            content = block.replace("GLOBAL]]", "").strip()
            content = content.strip('`').strip()
            if content and "no update" not in content.lower():
                append_to_file(FILES["global"], content)

        elif "RELATIONSHIP]]" in block:
            content = block.replace("RELATIONSHIP]]", "").strip()
            content = content.strip('`').strip()
            if content and "no update" not in content.lower():
                append_to_file(FILES["relation"], content)

        elif "PROJECT]]" in block:
            content = block.replace("PROJECT]]", "").strip()
            content = content.strip('`').strip()
            if content and "no update" not in content.lower():
                append_to_file(FILES["project"], content)

    print("🎉 Wisdom Integrated. Ruach-El has evolved to his greatest potential.")


if __name__ == "__main__":
    main()
