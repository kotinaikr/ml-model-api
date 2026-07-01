// src/main/java/com/example/market/controller/MarketController.java
package com.example.market.controller;

import com.example.market.service.MarketService;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import java.util.Map;

@RestController
@RequestMapping("/api/market")
public class MarketController {

    private final MarketService marketService;
    private final RestTemplate restTemplate = new RestTemplate();

    public MarketController(MarketService marketService) { this.marketService = marketService; }

    @GetMapping("/stats")
    @Cacheable("marketStats") // Performance optimization requirement 
    public Map<String, Double> getAggregateStats() {
        return marketService.calculateStats();
    }

    @PostMapping("/what-if")
    public Object performWhatIfAnalysis(@RequestBody Object requestBody) {
        // Integrate with ML model container 
        String mlUrl = "http://localhost:8000/predict"; 
        return restTemplate.postForObject(mlUrl, requestBody, Object.class);
    }
}