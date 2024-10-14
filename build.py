from mindmeld import configure_logs; configure_logs()
from mindmeld.components.nlp import NaturalLanguageProcessor
nlp = NaturalLanguageProcessor(app_path='myapp')
def build():
    nlp.build()
    nlp.dump()
    #nlp.domains['personal_disc_commands'].build()
    #nlp.domains['personal_disc_commands'].dump()
if __name__ == "__main__":
    build()