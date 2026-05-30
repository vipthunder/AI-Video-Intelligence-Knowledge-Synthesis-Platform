# AI Video Intelligence & Knowledge Synthesis Platform

An AI-powered platform that transforms local and YouTube videos into searchable knowledge using transcription, semantic search, Retrieval-Augmented Generation (RAG), and Gemini-powered  cross-question answering.

##  🎥 Demo Video
https://github.com/user-attachments/assets/419658dd-6463-4c48-b05a-2d187ae6c402

## Sysytem Architecture

                 ┌────────────────────┐
                 │   User Interface   │
                 │     Streamlit      │
                 └─────────┬──────────┘
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
 ┌─────────────────┐               ┌─────────────────┐
 │  Local Videos   │               │  YouTube URLs   │
 └────────┬────────┘               └────────┬────────┘
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
              ┌──────────────────┐
              │ Video Processing │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Audio Extraction │
              │     FFmpeg       │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Groq Whisper API │
              │  Transcription   │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Text Chunking    │
              │  Token Based     │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Gemini Embedding │
              │      Model       │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │     ChromaDB     │
              │ Vector Database  │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Semantic Search  │
              │    Retriever     │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ LangChain RAG    │
              │      LCEL        │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Gemini 2.5 Flash │
              │       LLM        │
              └────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Question Answer  │
              │ Knowledge Chat   │
              └──────────────────┘

##  Project Features 

- Upload local videos
- Process YouTube videos
- Groq Whisper transcription
- Gemini Embeddings
- ChromaDB Vector Database
- RAG-based Question Answering
- Multi-video processing
- Streamlit Interface

## Tech Stack Used

- Python
- Streamlit
- LangChain
- Gemini 2.5 Flash
- Gemini Embeddings
- ChromaDB
- Groq Whisper
- yt-dlp

##  Project Workflow

Video(local/youtube urls)
->
Audio Extraction
->
Transcription( Whisper AI)
->
Chunking
->
Embeddings(Gemini embedding)
->
ChromaDB
->
Retriever(mmr)
->
Gemini(LLM)
->
Answer and cross question 
