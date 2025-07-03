# 🎓 Educhain MCP Server

This project integrates the [Educhain](https://pypi.org/project/educhain/) library with [Claude's Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to provide a suite of educational tools powered by AI. It exposes local tools and resources such as MCQ generation, lesson plan creation, and multimedia-based question generation — all available within Claude's desktop environment.

---

## 🚀 Features

- 📝 Generate Multiple Choice Questions (MCQs)
- 🧠 Create structured lesson plans
- 📺 Generate questions from YouTube videos
- 📊 Generate questions from provided data source (e.g., text, pdf, url)
- 🎨 Support for prompt templates
- 🌐 Designed to work locally with Claude AI's Model Context Protocol (MCP)

---

## 📁 Folder Structure
```
claude-mcp-educhain/
├── tools/
│   ├── mcq_generator.py      # Tool: Generate MCQs
│   ├── lesson_plan_gen.py    # Resource: Generate lesson plans
│   ├── youtube_qna.py        # Tool: Questions from YouTube
│   └── ques_from_data.py     # Tool: Questions from data
├── mcp_server.py             # MCP server entry point
├── requirements.txt          # Python dependencies
├── sample_responses.txt      # Sample output (optional)
├── .env                      # Optional environment config
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

---

## 🧠 Available MCP Tools & Resources

| Name                                | Type      | File                 | Description                            |
|-------------------------------------|-----------|----------------------|----------------------------------------|
| `generate_multiple_choice_questions`| Tool      | `mcq_generator.py`   | Generate MCQs for a given topic        |
| `generate_lesson_plan`              | Tool      | `lesson_plan_gen.py` | Returns a structured lesson plan       |
| `generate_questions_from_youtube`   | Tool      | `youtube_qna.py`     | Generate questions from YouTube videos |
| `generate_questions_from_data`      | Tool      | `ques_from_data.py`  | Generate questions from provided data  |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/claude-mcp-educhain.git
cd claude-mcp-educhain
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API key (Google Gemini in this case)

Create a `.env` file and add your Google Gemini API Key.

---

## ▶️ Running the MCP Server

Normally, Claude MCP will launch your server automatically via the config file.

To run manually (for debugging):

```bash
python mcp_server.py
```

## 📚 Resources Used

- [Educhain Library Documentation](https://pypi.org/project/educhain/)  
  Comprehensive documentation for the Educhain Python library used for generating questions, lesson plans, and more.

- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)  
  Official documentation for Claude’s Model Context Protocol, which enables tool/resource integration in local AI environments.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
