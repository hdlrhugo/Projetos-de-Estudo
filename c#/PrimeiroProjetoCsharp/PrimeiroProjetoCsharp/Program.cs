using System;
using PrimeiroProjetoCsharp;   

namespace PrimeiroProjetoCsharp
{
    class Program
    {
        static void Main(String[] args) {

            Pessoa person = new Pessoa();
            person.nome = "Hugo";
            person.idade = 30;
            person.estado = "SP";

            var person2 = new Pessoa();
            person2.nome = "Andressa";
            person2.idade = 29;
            person2.estado = "PE";

            Console.WriteLine("OLA MUNDO!");
        }
    }

}
