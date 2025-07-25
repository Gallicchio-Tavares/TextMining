package textinhos;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Teste {
    public static void main(String[] args){
        String filePath = "textmining/MQD-1465-ALT.csv.csv";
        String lexicoPath = "textmining/AffectPT-br";
        
        Set<String> lexicon = readLexicon(lexicoPath);
        Map<String, Integer> wordFrequencyMap = new HashMap<>(); 
        Map<String, Integer> wordFrequencyMapLexico = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) { 
            String line;
            while ((line = br.readLine()) != null) {
                String[] words = line.split("[\s,.;!?\"]+");
                for (String word : words) {
                    word = word.toLowerCase();
                    wordFrequencyMap.put(word, wordFrequencyMap.getOrDefault(word, 0) + 1);
                    if (lexicon.contains(word)) {
                        wordFrequencyMapLexico.put(word, wordFrequencyMapLexico.getOrDefault(word, 0) + 1);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        List<Map.Entry<String, Integer>> sortedEntries = new ArrayList<>(wordFrequencyMap.entrySet());
        sortedEntries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

        List<Map.Entry<String, Integer>> sortedEntriesLexico = new ArrayList<>(wordFrequencyMapLexico.entrySet());
        sortedEntriesLexico.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

        int count = 0;
        for (Map.Entry<String, Integer> entry : sortedEntries) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
            count++;
            if (count == 100) {
                break;
            }
        }
    }

    private static Set<String> readLexicon(String lexiconPath) {
        Set<String> lexicon = new HashSet<>();
        try (BufferedReader br = new BufferedReader(new FileReader(lexiconPath))) {
            String line;
            while ((line = br.readLine()) != null) {
                lexicon.add(line.trim().toLowerCase());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lexicon;
    }

}
        // Passos:
        //  1 - Ler o arquivo CSV e extrair o conteúdo de texto. 
        //  2 - Dividir o texto em palavras.
        //  3 - Contar a frequência de ocorrência de cada palavra.
        //  4 - Classificar as palavras com base na contagem.
        //  5 - Exibir as 100 palavras mais frequentes em ordem decrescente.
