import pyautogui
import pygetwindow as gw
import time


TITULO_DA_JANELA = "PokeМMO" 


COMANDOS_TECLADO = [
  
    's', 's', 1, '2', 'w', 'z', 6,   # abre o mapa e seleciona o pokecenter   
                 
    'w', 'w', 2, 'w', 'w', 'w',  'w' , 'd' ,'d', 'd', 'w','z', 0.5,'z', 0.5 ,'z', 5, 'z', 0.5, 'z', # recupera a vida dos pokemons
         
    'a', 'a','a', 's', 's', 's', 's', 's', 's', 2, # sai do pokecenter 
      
    
    '1', 's', 's', 's', 's', 's', 's', 's', 'd', 'd', 's', 's', 'd', 'd', 'd', 's', 's', 'a', 'a', 's', 's', 's', 's', 's', 'd', 'd', 's', 's', 'a', 'a', 's',  's', 's', 's', 'd', 'd', 'd', 'd', 's', 's', 's', 's', 's', 's', 'a', 'a', '1',  'a', 'w', 'w',  # chega a caverna  
                          
]


def automatizar_tarefa():
  try:
    print(f"Procurando pela janela com o título: '{TITULO_DA_JANELA}'...")
        
       
    all_windows = gw.getAllTitles()
        
    window = None
    for title in all_windows:
      # Verifica se o TÍTULO_DA_JANELA está DENTRO do título da janela atual
            
      if TITULO_DA_JANELA in title:
        # Encontramos! Pegamos o objeto da janela pelo seu título completo
        window = gw.getWindowsWithTitle(title)[0]
        print(f"Janela encontrada com o título: '{title}'")
        break # Para o loop assim que encontrar

    if not window:
      print(f"Erro: Nenhuma janela contendo '{TITULO_DA_JANELA}' foi encontrada.")
      print("Verifique se o aplicativo está aberto.")
      return

    # 2. Ativa (foca) a janela
    print("Ativando a janela...")
    if not window.isActive:
      # Tenta restaurar se estiver minimizada e depois ativar
      if window.isMinimized:
          window.restore()
      window.activate()
        
    # Espera 1 segundo para garantir que a janela está 100% focada
    time.sleep(1)

    # 3. Executa os comandos do teclado
    print("Enviando comandos do teclado...")
    for comando in COMANDOS_TECLADO:
      if isinstance(comando, str):
        # --- Se for uma TECLA (string) ---
        print(f"  - Pressionando: '{comando}'")
        pyautogui.keyDown(comando)
        pyautogui.keyUp(comando)
        pyautogui.press(comando)
            
      elif isinstance(comando, (int,float)):
        # --- Se for uma PAUSA (número) ---
        print(f"  - Pausando por: {comando}s")
        time.sleep(comando)

      time.sleep(0.1)
      
    print("\nAutomação concluída com sucesso!")

  except Exception as e:
      print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    #while True:
      print("Iniciando a automação em 3 segundos...")
      time.sleep(3)
      
      automatizar_tarefa()