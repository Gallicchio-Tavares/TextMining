package TextMining.tarefa1;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Freq100 {
    public static void main(String[] args){
        String arquivoPath = "TextMining/tarefa1/MQD-1465-ALT.csv.csv";

        Map<String, Integer> palavraFreqMap = new HashMap<>(); //Criar um Map para armazenar a contagem de frequência das palavras e usar um HashMap para associar cada palavra a sua contagem.

        try (BufferedReader br = new BufferedReader(new FileReader(arquivoPath))) { // abrir e ler o arquivo usando um BufferedReader
            // Para cada linha lida, dividimos a linha em palavras usando uma expressão regular que considera espaços, vírgulas, pontos e outros caracteres de pontuação como separadores. 
            // Para cada palavra encontrada, normalizamos para minúsculas, verificamos se ela já existe no mapa e atualizamos sua contagem. 
            // Se não existir, adicionamos a palavra ao mapa com contagem inicial 1.
            String linha;
            while ((linha = br.readLine()) != null) { // lendo a linha
                String[] palavras = linha.split("[\s,.;!?\"]+"); // devemos separar quando houver pontuação
                for (String palavra : palavras) {
                    palavra = palavra.toLowerCase(); // Deixar todas as palavras minúsculas
                    if(!removerStopWords(palavra)){
                        palavraFreqMap.put(palavra, palavraFreqMap.getOrDefault(palavra, 0) + 1); //atualizar a contagem de ocorrências de uma palavra no mapa
                    }
                    // incrementando a contagem se a palavra já estiver no mapa
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        List<Map.Entry<String, Integer>> sortedEntries = new ArrayList<>(palavraFreqMap.entrySet());
        sortedEntries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

        int contador = 0;
        for (Map.Entry<String, Integer> entry : sortedEntries) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
            contador++;
            if (contador == 100) {
                break;
            }
        }
    }

    private static boolean removerStopWords(String palavra) {
        List<String> stopWords = Arrays.asList("a", "as", "o", "os", "ao", "um", "uma", "uns", "umas", "e", "mas", "ou", "que", "quem", "qual", "onde", "cujo", "cujos", "cuja", "cujas", "quais", "quando", "quanto", "quantos", "quanta", "quantas", "da", "de", "do", "dos", "das", "em", "na", "no", "com", "para", "pra", "por", "pelo", "pela");
        return stopWords.contains(palavra);
    }

    /*
     * eu vou considerar que stopwords são artigos definidos e indefinidos, pronomes relativos, algumas preposições e conjunções.
     * Não vou colocar tudo por enquanto pq é mta coisa
     */
}
