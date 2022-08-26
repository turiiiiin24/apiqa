from flask import Flask
class CustomMessageEE():
    """ Clase para el menejo de mensajes. """

    LETTER_BY_NUMBERS = {
       
            '1':'K',
            '2':'C',
            '3':'J',
            '4':'X',
            '5':'B',
            '6':'Z',
            '7':'E',
            '8':'L',
            '9':'V',
            '0':'W', 
    }

    def __init__(self, message):
        """ Constructor. """
        self.message = message


    def return_letter_associated_with_umber(self, letter):
        """ Método para verificar si una letra tiene asociado un número. """
        l = letter.upper()
        if l in self.LETTER_BY_NUMBERS:
            return self.LETTER_BY_NUMBERS[l]
        else:
            return l


    def substitute_letters_by_numbers(self):
        """ Método para convertir un mensaje a un mensaje combinado con números. """
        words = self.message.split(" ")
        new_message = []

        for word in words:
            new_word = ''
            for letter in word:
                new_word += self.return_letter_associated_with_umber(letter)

            new_message.append(new_word)
        
        return ' '.join(new_message)





app= Flask(__name__)
@app.route('/app/v1/descriptar/<id>')
def start():
        if(id=="8"):
            #  inst=users_action()
            #  m=des.CustomMessage(id)
            #  new_message = des.substitute_numbers_by_letters()
             return "IF" 
        else:
            m = CustomMessage(id)
            new_message = m.substitute_letters_by_numbers()
              
            return "El numero de tarjeta essirve?: "+new_message
