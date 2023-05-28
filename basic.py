import openai

openai.api_key = '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'

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": 
             "essay on penguins"}]
)

# Print out the whole output dictionary
print(output)

# Get the output text only
print(output['choices'][0]['message']['content'])