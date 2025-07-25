package textinhos;

public class SeparadorPalavras {
    public static void main(String[] args) {
        String sentence = "Olá, \"mundo\"! Como vai?";
        System.out.println(sentence);

        String[] words = sentence.split("[\\s,.;!?\"]+");
        
        for (String word : words) {
            System.out.println(word);
        }
    }
}

/*
 * \\s significa os espaços
 * ,.;!? são as diferentes pontuações 
 * \" representa o caracter das aspas duplas. se n colocar a contrabarra antes dá ruim
 *  o + indica que a expressão anterior deve corresponder a um ou mais caracteres em sequência,
 * Isso permite que vários caracteres de separação sejam tratados como um único separador
 */