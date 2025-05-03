from jarvis_core import iniciar_jarvis
from interface import InterfaceVisual
import threading

if __name__ == "__main__":
    interface = InterfaceVisual()
    thread_jarvis = threading.Thread(target=iniciar_jarvis, args=(interface,))
    thread_jarvis.start()
    interface.iniciar()
