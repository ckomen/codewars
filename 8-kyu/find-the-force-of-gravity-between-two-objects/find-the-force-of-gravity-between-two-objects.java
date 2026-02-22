public class Solution {
    public static double solution(double[] arrVal, String[] arrUnit) {
        final double G = 6.67e-11;
​
        java.util.Map<String, Double> massConversions = new java.util.HashMap<>();
        massConversions.put("kg",  1.0);
        massConversions.put("g",   1e-3);
        massConversions.put("mg",  1e-6);
        massConversions.put("μg",  1e-9);
        massConversions.put("lb",  0.453592);
​
        java.util.Map<String, Double> distanceConversions = new java.util.HashMap<>();
        distanceConversions.put("m",  1.0);
        distanceConversions.put("cm", 1e-2);
        distanceConversions.put("mm", 1e-3);
        distanceConversions.put("μm", 1e-6);
        distanceConversions.put("ft", 0.3048);
​
        double m1 = arrVal[0] * massConversions.get(arrUnit[0]);
        double m2 = arrVal[1] * massConversions.get(arrUnit[1]);
        double r  = arrVal[2] * distanceConversions.get(arrUnit[2]);
​
        return G * m1 * m2 / (r * r);
    }
}
​