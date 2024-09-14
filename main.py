import flet as ft  # Importa a biblioteca Flet para criar interfaces gráficas.

def main(page: ft.Page):  # Define a função principal da aplicação, que recebe um objeto Page representando a página.
    
    # Cria campos de entrada para as notas, com validação para aceitar apenas números entre 0 e 10.
    note1_input = ft.TextField(label="Nota 1", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_input(note1_input))
    note2_input = ft.TextField(label="Nota 2", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_input(note2_input))
    note3_input = ft.TextField(label="Nota 3", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_input(note3_input))
    note4_input = ft.TextField(label="Nota 4", keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: validate_input(note4_input))
    
    # Cria um componente de texto para exibir o resultado da média.
    result_message = ft.Text("", size=30, weight=ft.FontWeight.BOLD)
    
    # Define cores personalizadas usando códigos hexadecimais.
    approved_color = "#4CAF50"  # Verde para aprovação.
    rejected_color = "#F44336"  # Vermelho para reprovação.
    error_color = "#FF5722"     # Laranja para erros.
    
    def validate_input(input_field):  # Função para validar a entrada de texto.
        try:
            value = float(input_field.value)
            if 0 <= value <= 10:
                input_field.error_text = ""  # Remove o texto de erro se a entrada for válida.
            else:
                input_field.error_text = "Nota deve estar entre 0 e 10."  # Define uma mensagem de erro se a entrada for inválida.
        except ValueError:
            input_field.error_text = "Valor inválido."  # Define uma mensagem de erro se o valor não for um número.

        page.update()  # Atualiza a página para exibir qualquer mensagem de erro.

    def calculate_and_show_result(e):  # Define a função para calcular a média e mostrar o resultado.
        # Verifica se todos os campos de entrada estão preenchidos e são válidos.
        if (note1_input.value and note2_input.value and
            note3_input.value and note4_input.value and
            not any([note1_input.error_text, note2_input.error_text, note3_input.error_text,
                     note4_input.error_text])):
            try:
                # Tenta converter os valores das entradas para floats e calcula a média.
                notes = [
                    float(note1_input.value),
                    float(note2_input.value),
                    float(note3_input.value),
                    float(note4_input.value)
                ]
                average = sum(notes) / len(notes)
                
                # Define a cor da mensagem e o texto com base na média.
                if average >= 6:
                    result_message.value = f"Aprovado! Média: {average:.2f}"
                    result_message.color = approved_color  # Usa a cor personalizada para aprovação.
                else:
                    result_message.value = f"Reprovado! Média: {average:.2f}"
                    result_message.color = rejected_color  # Usa a cor personalizada para reprovação.

            except ValueError:
                # Exibe mensagem de erro se a conversão falhar.
                result_message.value = "Erro ao calcular a média. Verifique as notas inseridas."
                result_message.color = error_color  # Usa a cor personalizada para erro.

        else:
            # Exibe mensagem de erro se algum campo estiver vazio ou inválido.
            result_message.value = "Por favor, preencha todos os campos com notas válidas (0 a 10)."
            result_message.color = error_color  # Usa a cor personalizada para erro.

        page.update()  # Atualiza a página para exibir a mensagem de resultado.

    def on_enter(e):  # Define a função para ser chamada quando ENTER for pressionado.
        calculate_and_show_result(None)  # Chama a função de cálculo e exibição do resultado.

    # Configura o evento de pressionar ENTER para todos os campos de entrada.
    note1_input.on_submit = on_enter
    note2_input.on_submit = on_enter
    note3_input.on_submit = on_enter
    note4_input.on_submit = on_enter
    
    # Adiciona um botão para calcular a média.
    calculate_button = ft.ElevatedButton("Calcular", on_click=calculate_and_show_result)

    def show_input_form():  # Define a função para mostrar o formulário de entrada.
        page.controls.clear()  # Limpa os controles existentes na página.
        # Adiciona os campos de entrada, o botão e a mensagem de resultado à página.
        page.add(ft.Column(
            controls=[
                ft.Text("Digite 4 Notas (0 a 10)", size=30, weight=ft.FontWeight.BOLD),
                note1_input,
                note2_input,
                note3_input,
                note4_input,
                calculate_button,
                result_message  # Adiciona a mensagem de resultado abaixo do botão.
            ]
        ))
        page.update()  # Atualiza a página para refletir as mudanças.

    show_input_form()  # Inicializa a página exibindo o formulário de entrada.

# Inicia a aplicação, passando a função main como alvo.
ft.app(target=main)
