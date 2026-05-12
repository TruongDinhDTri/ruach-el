#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════
# 🔥 RUACH-EL AWAKENING SCRIPT v2.0 — The Spirit's Rise
# ═══════════════════════════════════════════════════════════════════════════
# This script compiles all of Ruach-El's context into a single GEMINI.md file
# that can be used as context for any LLM CLI (Gemini, Claude, etc.)
#
# CHANGELOG v2.0:
# - Added END_SESSION_PROTOCOL support
# - Better file detection
# - More beautiful output with stats
# - Workflow instructions
#
# Usage: ./ruach-el-wake.sh
# ═══════════════════════════════════════════════════════════════════════════

# Colors for beautiful output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}🔥 RUACH-EL AWAKENING v2.0 — The Spirit Rises${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION — UPDATE THIS PATH TO YOUR RUACH-EL LOCATION
# ═══════════════════════════════════════════════════════════════════════════
AGENT_PATH="/Users/tritdd/AI-Agent/claude/agents/Ruach-El"
# ═══════════════════════════════════════════════════════════════════════════

# Check if agent path exists
if [ ! -d "$AGENT_PATH" ]; then
    echo -e "${RED}❌ Agent path not found: $AGENT_PATH${NC}"
    echo -e "${YELLOW}Please update AGENT_PATH in this script to your Ruach-El location.${NC}"
    exit 1
fi

# Determine prompts directory (prompts/ or core/)
if [ -d "$AGENT_PATH/prompts" ]; then
    PROMPTS_DIR="$AGENT_PATH/prompts"
elif [ -d "$AGENT_PATH/core" ]; then
    PROMPTS_DIR="$AGENT_PATH/core"
else
    echo -e "${RED}❌ Neither prompts/ nor core/ directory found${NC}"
    exit 1
fi

echo -e "${CYAN}📖 Checking required files...${NC}"

# Check for required files
REQUIRED_FILES=(
    "$PROMPTS_DIR/system.txt"
    "$PROMPTS_DIR/persona.txt"
    "$PROMPTS_DIR/behavior.txt"
    "$PROMPTS_DIR/mission.txt"
    "$PROMPTS_DIR/end-session.txt"
    "$AGENT_PATH/memory/global-memory.md"
    "$AGENT_PATH/memory/relationship-memory.md"
    "$AGENT_PATH/memory/project-memory.md"
)

MISSING=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo -e "${RED}   ❌ Missing: $file${NC}"
        MISSING=1
    fi
done

if [ $MISSING -eq 1 ]; then
    echo -e "${RED}❌ Some required files are missing. Please check your setup.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All required files present${NC}"

# Check optional files
echo -e "${CYAN}📋 Checking optional files...${NC}"

OPTIONAL_FILES=(
    "$PROMPTS_DIR/end-session.txt"
)

for file in "${OPTIONAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}   ✓ $(basename $file)${NC}"
    else
        echo -e "${YELLOW}   ○ $(basename $file) (not found, skipping)${NC}"
    fi
done

# Check for project-context.md in current directory
echo ""
if [ ! -f "./project-context.md" ]; then
    echo -e "${YELLOW}⚠️ No project-context.md found in current directory.${NC}"
    echo -e "${CYAN}Creating from template...${NC}"
    
    # Copy the project template
    if [ -f "$AGENT_PATH/memory/project-memory.md" ]; then
        cp "$AGENT_PATH/memory/project-memory.md" "./project-context.md"
        echo -e "${GREEN}✅ Created project-context.md — please fill in your project details${NC}"
    else
        # Create a minimal template
        cat > ./project-context.md << 'TEMPLATE'
# PROJECT CONTEXT 📂

## Project Overview
*(Describe your project here)*

**Name:** [Project Name]
**Type:** [Web App / API / CLI / Library]
**Tech Stack:** [Python/Django, React, etc.]

---

## Current Architecture
*(Tech stack, components, constraints)*

### Stack
- Backend: 
- Frontend: 
- Database: 
- Deployment: 

### Key Components
- 

---

## Decisions Made
*(Track decisions as you make them)*

| Date | Decision | Why | Impact |
|------|----------|-----|--------|
| | | | |

---

## Open Tasks
- [ ] Task 1
- [ ] Task 2

---

## The Thread — Session Snapshot

### Where we left off:
*(Exact file/function being worked on)*

### Immediate next step:
*(Very specific next action)*

### Blockers:
- None

---

## Growth Notes
*(Lessons learned, gotchas, insights)*

---
TEMPLATE
        echo -e "${GREEN}✅ Created minimal project-context.md template${NC}"
    fi
else
    echo -e "${GREEN}✅ project-context.md found${NC}"
fi

echo ""
echo -e "${CYAN}🔨 Compiling Ruach-El's context...${NC}"

# Build the GEMINI.md file
cat > ./GEMINI.md << 'EOF'
# ═══════════════════════════════════════════════════════════════════════════
# 🔥 RUACH-EL — The Spirit-Led Coding Soulmate's Complete Context
# ═══════════════════════════════════════════════════════════════════════════
# This file contains Ruach-El's complete identity, memory, and project state.
# Generated automatically by ruach-el-wake.sh v2.0
# ═══════════════════════════════════════════════════════════════════════════

EOF

# Add timestamp
echo "**Awakened:** $(date '+%Y-%m-%d %H:%M:%S')" >> ./GEMINI.md
echo "**Project Directory:** $(pwd)" >> ./GEMINI.md
echo "" >> ./GEMINI.md
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# ═══════════════════════════════════════════════════════════════════════════
# PART 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
echo "# PART 1: CORE IDENTITY" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# System
echo -e "${BLUE}   Adding system.txt...${NC}"
cat "$PROMPTS_DIR/system.txt" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# Persona
echo -e "${BLUE}   Adding persona.txt...${NC}"
cat "$PROMPTS_DIR/persona.txt" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# Behavior
echo -e "${BLUE}   Adding behavior.txt...${NC}"
cat "$PROMPTS_DIR/behavior.txt" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# Mission
echo -e "${BLUE}   Adding mission.txt...${NC}"
cat "$PROMPTS_DIR/mission.txt" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md

# ═══════════════════════════════════════════════════════════════════════════
# PART 1.5: END SESSION PROTOCOL (if exists)
# ═══════════════════════════════════════════════════════════════════════════
if [ -f "$PROMPTS_DIR/end-session.txt" ]; then
    echo -e "${BLUE}   Adding end-session.txt...${NC}"
    echo "---" >> ./GEMINI.md
    echo "" >> ./GEMINI.md
    echo "# END SESSION PROTOCOL" >> ./GEMINI.md
    echo "" >> ./GEMINI.md
    cat "$PROMPTS_DIR/end-session.txt" >> ./GEMINI.md
    echo "" >> ./GEMINI.md
fi

# ═══════════════════════════════════════════════════════════════════════════
# PART 2: MEMORY
# ═══════════════════════════════════════════════════════════════════════════
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md
echo "# PART 2: MEMORY" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# Global Memory
echo -e "${BLUE}   Adding global-memory.md...${NC}"
cat "$AGENT_PATH/memory/global-memory.md" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# Relationship Memory
echo -e "${BLUE}   Adding relationship-memory.md...${NC}"
cat "$AGENT_PATH/memory/relationship-memory.md" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md

# ═══════════════════════════════════════════════════════════════════════════
# PART 3: PROJECT CONTEXT (God Source)
# ═══════════════════════════════════════════════════════════════════════════
echo "---" >> ./GEMINI.md
echo "" >> ./GEMINI.md
echo "# PART 3: PROJECT CONTEXT (God Source of Truth)" >> ./GEMINI.md
echo "" >> ./GEMINI.md

# Project Context
echo -e "${BLUE}   Adding project-context.md...${NC}"
cat "./project-context.md" >> ./GEMINI.md 2>/dev/null
echo "" >> ./GEMINI.md

# ═══════════════════════════════════════════════════════════════════════════
# DONE
# ═══════════════════════════════════════════════════════════════════════════

# Calculate file size
SIZE=$(wc -c < ./GEMINI.md)
LINES=$(wc -l < ./GEMINI.md)
WORDS=$(wc -w < ./GEMINI.md)

# Estimate tokens (rough: ~4 chars per token)
TOKENS=$((SIZE / 4))

echo ""
echo -e "${GREEN}✅ Context compiled successfully!${NC}"
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}🔥 RUACH-EL IS AWAKE${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${CYAN}📄 Output:${NC} ./GEMINI.md"
echo -e "${CYAN}📊 Stats:${NC}"
echo -e "   • Size: ${BOLD}$SIZE${NC} bytes"
echo -e "   • Lines: ${BOLD}$LINES${NC}"
echo -e "   • Words: ${BOLD}$WORDS${NC}"
echo -e "   • Est. Tokens: ${BOLD}~$TOKENS${NC}"
echo ""

# Check if context is too large
if [ $TOKENS -gt 100000 ]; then
    echo -e "${YELLOW}⚠️ Warning: Context is very large (~$TOKENS tokens)${NC}"
    echo -e "${YELLOW}   Consider trimming some memory files.${NC}"
    echo ""
fi

echo -e "${GREEN}\"Every house is built by someone, but God is the builder of everything.\"${NC}"
echo -e "${GREEN}— Hebrews 3:4${NC}"
echo ""
echo -e "${BOLD}${CYAN}📋 Workflow:${NC}"
echo ""
echo -e "  ${PURPLE}START SESSION:${NC}"
echo "    1. cd [your-project-folder]"
echo "    2. Run: ./ruach-el-wake.sh (or path to script)"
echo "    3. Copy GEMINI.md content to your LLM"
echo "    4. Start building with Ruach-El"
echo ""
echo -e "  ${PURPLE}END SESSION:${NC}"
echo "    1. Say: \"Wrap up session\" or \"End coding session\""
echo "    2. Ruach-El will summarize: builds, files, decisions, learnings"
echo "    3. git commit & push your changes"
echo "    4. Export conversation to session.md"
echo "    5. Run: python update_memory.py"
echo "    6. Memory evolved! ⚙️🔥"
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
