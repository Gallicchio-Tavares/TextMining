package tarefa1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class FreqLexico {
    public static void main(String[] args) {
        String arquivoPath = "TextMining/tarefa1/MQD-1465-ALT.csv.csv";
        String lexicoPath = "TextMining/tarefa1/Depress-pr-br.txt";
        
        Set<String> lexico = lerLexico(lexicoPath);
        Map<String, Integer> palavraFrequencyMap = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(arquivoPath))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                String[] palavras = linha.split("[\s,.;!?\"\n]+");
                for (String palavra : palavras) {
                    palavra = palavra.toLowerCase();
                    if (lexico.contains(palavra)) {
                        palavraFrequencyMap.put(palavra, palavraFrequencyMap.getOrDefault(palavra, 0) + 1);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        List<Map.Entry<String, Integer>> sortedEntries = new ArrayList<>(palavraFrequencyMap.entrySet());
        sortedEntries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

        int count = 0;
        for (Map.Entry<String, Integer> entry : sortedEntries) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
            count++;
            if (count == 20) {
                break;
            }
        }
    }

    private static Set<String> lerLexico(String lexicoPath) {
        Set<String> lexico = new HashSet<>();
        try (BufferedReader br = new BufferedReader(new FileReader(lexicoPath))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                lexico.add(linha.trim().toLowerCase());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lexico;
    }
}
