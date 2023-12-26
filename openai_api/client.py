from openai import OpenAI


def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    prompt = prompt.format(brand, model, year)

    client = OpenAI(
        api_key=''
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ],
        model='gpt-3.5-turbo',
    )
    return chat_completion.choices[0].message.content

# def get_car_ai_bio(model, brand, year):
#     prompt = '''
#     Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
#     '''
#     openai.api_key = ''
#     prompt = prompt.format(brand, model, year)
#     response = openai.Completion.create(
#         model = 'text-davinci-003',
#         prompt = prompt,
#         max_tokens=1000,
#     )
#     return response['choices'][0]['text']

