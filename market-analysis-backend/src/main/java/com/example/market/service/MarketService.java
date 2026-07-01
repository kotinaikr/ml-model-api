// src/main/java/com/example/market/service/MarketService.java
package com.example.market.service;

import com.example.market.model.Property;
import org.springframework.stereotype.Service;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class MarketService {
    // In a real scenario, load this from the CSV file
    private List<Property> properties = new ArrayList<>(); 

    public Map<String, Double> calculateStats() {
        double avgPrice = properties.stream().mapToDouble(Property::price).average().orElse(0.0);
        double maxPrice = properties.stream().mapToDouble(Property::price).max().orElse(0.0);
        
        Map<String, Double> stats = new HashMap<>();
        stats.put("averagePrice", avgPrice);
        stats.put("maxPrice", maxPrice);
        return stats;
    }
}