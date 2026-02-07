# Import openai Python library for LLM use
import openai
import os

# Set openai key as OPENAI_API_KEY set in .env using os Python library
openai.api_key = os.getenv("OPENAI_API_KEY")

# Import clean_data from main
def generate_summary(clean_data):

    # If clean_data is empty then return the message for that
    if clean_data.empty:
        return "No data to summarize."

    # Create the LLM prompt to generate the report
    # Inserts clean_data into the prompt for the LLM to use
    llm_summary_prompt = f"""Analyze the following campaign performance data and summarize trends:
    
    {clean_data.to_markdown(index=False)}

    Focus on cost efficiency, top-performing campaigns, and recommendations."""

    # Uses try and except in case the openai library encounters an error on responding
    try:
        response = openai.ChatCompletion.create(
            # Model can be updated
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data analyst for digital marketing."},
                {"role": "user", "content": llm_summary_prompt}
            ],
            temperature=0.4
        )
        # return response message from the choices returned
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Summary generation failed: {e}"
