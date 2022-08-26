from flask import Flask
class CustomMessage():
    """ Clase para el menejo de mensajes. """

    LETTER_BY_NUMBERS = {
       
            'K':'1',
            'C':'2',
            'J':'3',
            'X':'4',
            'B':'5',
            'Z':'6',
            'E':'7',
            'L':'8',
            'V':'9',
            'W':'0', 
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




def start():
    """ Método para iniciar el proceso de conversión de letras a números. """
    message = str(input("Escribe tu mensaje: "))
    m = CustomMessage(message)
    new_message = m.substitute_letters_by_numbers()
    print("<------------------------------------------------->")
    print(new_message)
    print("<------------------------------------------------->")




app= Flask(__name__)

@app.route('/app/v1/descriptar/<id>')
def users_action(id):
        if(id=="8"):
             m = CustomMessage(id)
             new_message = m.substitute_letters_by_numbers()
             return "IF"+new_message
        else:
            m = CustomMessage(id)
            new_message = m.substitute_letters_by_numbers()
            return "El numero de tarjeta es: "+new_message

app.run(debug=True,port=8080)
