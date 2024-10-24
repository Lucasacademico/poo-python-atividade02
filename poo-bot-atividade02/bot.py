from botcity.web import WebBot, Browser, By
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# lib chromedriver
from webdriver_manager.chrome import ChromeDriverManager

class Produto:
    qtd_produto = [] 
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.qtd_produto.append(self)

    def exibir_informacoes(self):
        print(f'- Nome: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}')

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f'Preço atualizado para R$ {self.preco:.2f}')

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
        print(f'Quantidade alterada para {self.quantidade}')


def iniciar_bot():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    return bot


def instanciar_produtos():
    produto1 = Produto('Placa de vídeo', 4531.48, 5)
    produto2 = Produto('Memória Ram', 485.23, 15)
    
    # Atualizações de preço e quantidade
    produto1.atualizar_preco(4200.99)
    produto1.atualizar_quantidade(9)
    
    # Exibir informações dos produtos
    produto1.exibir_informacoes()
    produto2.exibir_informacoes()
    
    return produto1, produto2 # Retornar a quantidade de instâncias


def preencher_formulario(bot):
    bot.browse(r"C:\Users\lrand\OneDrive\Área de Trabalho\Atividade 02\poo-bot-atividade02\index.html")
    for produto in Produto.qtd_produto:
        bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(produto.nome)
        bot.wait(1000)
        bot.find_element('//*[@id="preco"]', By.XPATH).send_keys(f'{produto.preco:.2f}')
        bot.wait(1000)
        bot.find_element('//*[@id="quantidade"]', By.XPATH).send_keys(produto.quantidade)
        bot.wait(1000)
        bot.find_element('/html/body/form/input[4]', By.XPATH).click()
    bot.wait(2000)


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Chamada de funções
    bot = iniciar_bot()
    instanciar_produtos()  # Instanciar produtos
    preencher_formulario(bot)  # Preencher formulário
    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
