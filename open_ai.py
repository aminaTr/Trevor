import os
import openai
from config import apikey

openai.api_key = apikey


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-80xSrjSgUGqmMJFhHXxtxdPZ6HXiV",
  "object": "text_completion",
  "created": 1695239273,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject: Resigning from my position\n\nDear [Name of Boss],\n\nI wanted to inform you that I am resigning from my position with [Company Name] effective [date].\n\nI have enjoyed my time working here and am grateful for the opportunities you have given me. Unfortunately, due to personal reasons, I have decided that now is the right time for me to pursue other opportunities.\n\nI will do my best to help transition my duties to a new team member and ensure that the work is completed prior to my last day. If there is any way that I can be of assistance in the meantime, please let me know.\n\nThank you again for welcoming me to the team and for all of the opportunities you have given me.\n\nSincerely,\n\n[Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 166,
    "total_tokens": 175
  }
}
'''

