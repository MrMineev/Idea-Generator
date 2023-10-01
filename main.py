import openai
import os
import rich

from ideas import Idea, parse_ideas
from google_trends import get_trend, sort_by_popularity

def get_prompt():
    return open("prompt.txt", "r").read()

def init_openai():
    openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response['choices'][0]['text']

    return answer

def main():
    init_openai()
    response = get_response(get_prompt())
    rich.print(response)
    ideas = parse_ideas(response)
    rich.print(ideas)

    print()

    for idea in ideas:
        rich.print(f"IDEA = {idea.s}")
        get_trend(idea.s)
        print()
        print()

    ideas_s = []
    for idea in ideas:
        ideas_s.append(idea.s)

    rich.print(sort_by_popularity(ideas_s))

if __name__ == '__main__':
    main()





