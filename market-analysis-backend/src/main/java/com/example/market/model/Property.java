// src/main/java/com/example/market/model/Property.java
package com.example.market.model;

public record Property(
    double squareFootage, int bedrooms, double bathrooms, 
    int yearBuilt, double lotSize, double distanceToCityCenter, 
    double schoolRating, double price
) {}