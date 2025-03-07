from openai import OpenAI
#open ai key ke liye paisa lagega toh chalegaa


client = OpenAI(
    api_key="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"
)    

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant assistant made to help your boss."},
        {
            "role": "user",
            "content": "what is coding"
        }
    ]
)

print(completion.choices[0].message)