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