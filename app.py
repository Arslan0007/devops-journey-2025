import streamlit as st
from textblob import TextBlob

# Page Configuration
st.set_page_config(
    page_title="The Gist",
    page_icon="📝",
    layout="centered"
)

# Header
st.title("📝 The Gist")
st.subheader("Digital Declutter Assistant")
st.write("Paste your text below to extract action items and analyze urgency.")

# Input Area
text_input = st.text_area("Input Text", height=200, placeholder="Paste your email, message, or document here...")

# Analysis Logic
if st.button("Get the Gist"):
    if text_input:
        # Create TextBlob object for processing
        blob = TextBlob(text_input)
        
        # --- 1. Urgency Logic (Keyword Heuristic) ---
        urgency_score = 0
        urgent_keywords = ['urgent', 'asap', 'deadline', 'immediately', 'important', 'priority']
        
        for word in urgent_keywords:
            if word in text_input.lower():
                urgency_score += 1
        
        if urgency_score >= 2:
            urgency_level = "High 🔴"
        elif urgency_score == 1:
            urgency_level = "Medium 🟡"
        else:
            urgency_level = "Low 🟢"

        # --- 2. Action Item Extraction (Sentence Analysis) ---
        action_keywords = ['need to', 'must', 'please', 'should', 'don\'t forget', 'ensure']
        actions = []
        
        for sentence in blob.sentences:
            s_str = str(sentence)
            # Check if sentence contains action keywords
            for k in action_keywords:
                if k in s_str.lower():
                    actions.append(s_str)
                    break # Avoid duplicates if multiple keywords exist in one sentence

        # --- Display Results ---
        st.divider()
        
        # Metrics Row
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Urgency", urgency_level)
        with col2:
            st.metric("Word Count", len(text_input.split()))
        with col3:
            st.metric("Sentences", len(blob.sentences))

        # Action Items
        st.subheader("📋 Detected Action Items")
        if actions:
            for action in actions:
                st.success(f"• {action}")
        else:
            st.info("No specific action items detected based on keywords.")

        # Sentiment Analysis (Bonus)
        st.subheader("🧠 Tone Analysis")
        sentiment = blob.sentiment.polarity
        if sentiment > 0.1:
            st.write("Tone: **Positive / Constructive**")
        elif sentiment < -0.1:
            st.write("Tone: **Negative / Critical**")
        else:
            st.write("Tone: **Neutral**")

    else:
        st.warning("⚠️ Please enter some text to analyze.")

# Footer
st.divider()
st.caption("🚀 The Gist v0.1 | Built for the 2025 DevOps Journey")