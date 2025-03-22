import gradio as gr
import requests

# Função de tradução (usando a API MyMemory)
def translate_text(text):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=pt|en"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data['responseStatus'] == 200:
        return data['responseData']['translatedText']
    else:
        return "Erro na tradução."

# Interface Gradio
iface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=2, placeholder="Digite o texto em português aqui..."),
    outputs="text",
    title="Tradutor Português-Inglês",
    description="Traduz texto de português para inglês."
)

if __name__ == '__main__':
    iface.launch()
