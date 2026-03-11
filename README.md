## Overview
This laboratory exercise performs spatial statistical analysis, focusing on spatial autocorrelation using Moran's I.

## Environment Setup
- Python 3.x
- PostgreSQL with PostGIS
- GeoPandas, SQLAlchemy, psycopg2, PySAL, numpy

## How to Run
1. Activate the virtual environment
2. Run `analysis.py` to run the full spatial statistical analysis pipeline

## Outputs
- GeoJSON of spatial clusters
- Visualization of resulting spatial clusters

## Reflections - Part D2
1. In the spatial weights graph, the parcel centroids represent the spatial units of analysis (which are represented as nodes in the graph). They are they units that could be considered "neighbors" or not. Meanwhile, the lines (corresponding to the edges of the graph)represent the "neighbor-ness" of two different parcels. The presence of a line means they are neighbors (for a given weights method), while the absence means they are not.
2. Contiguity weights created the densest neighbor graphs, primarily because some parcels bordered dozens of other parcels (e.g., buffer areas, road ROW, etc.). Meanwhile, at first glance, distance-based and KNN-based weights had similar-looking densities. However, large parcels had few or no neighbors under distance-based weighting (since their centroids are far from other parcels), while smaller residential parcels had very many neighbors. The picture is more balanced under KNN, which forces all parcels to have a certain number of neighbors.
3. Increasing the distance threshold makes the neighbor graph much denser, since each parcel has a wider radius within which it can claim neighbors. A similar effect can be observed with raising K in KNN-based weighting. However, for distance-based weighting, larger parcels remain islands (until the threshold is raised high enough for other centroids to reach theirs).
4. Roughly, yes. Increasing K or the distance threshold create a denser spatial network, because each parcel can have more neighbors.
5. Since the parcels are represented as an areal dataset that fully cover the AOI, thus making them properly border each other, contiguity-based weights might be the most appropriate. It makes sense that large or long parcels have many neighbors, as do smaller parcels in denser areas, while isolated parcels have fewer neighbors.
6. Visualizing the neighbor graph allows us to sense-check our definition of "neighbor-ness", ensuring it is appropriate for our datasets and research questions before we perform any further statistical analysis.

## Reflections - Part E2
1. A positive Moran's I indicate the presence of clustering (i.e., positive spatial autocorrelation). This means that attribute values of neighboring parcels are likely to be more similar to each other (vs. non-neighbors).
2. The p-value is important to assess the statistical significance of the clustering/dispersion approved. It is a measure of the probability that the observed result (in our case the "neighbor-ness") is due merely to random chance. A low p-value means we have very high confidence that this "neighbor-ness" is not random, and thus statistically significant.
3. A Moran's I value near zero would suggest a random spatial pattern, with no discernible trend of either clustering or dispersion.
4. The attribute is the property of the spatial units whose spatial distribution & pattern is being measured. Different attributes have their own patterns of distribution, and thus may lead to differing Moran's I values (i.e., different degrees of "neighbor-nes").
5. Analyzing different attributes may or may not lead to differing results in spatial autocorrelation. For example, the global Moran's I for `"ass_ass_va"` is ~0.33, which is slighly higher than the ~0.28 for `"ass_market"`. This means that the former attribute has a slightly more clustered distribution of values.
6. Moran's I requires the spatial weights matrix to define which spatial units can be considered neighbors. It also requires a specific attribute variable, because its purpose is to measure the similarity of this attribute's values for spatial units considered "neighbors" by the spatial weights matrix.

## Reflections - Part F4
1. Global Moran's I is a measure of the similarity of attribute values among neighbors (i.e., spatial autocorrelation) for the whole dataset. Roughly, it tells us whether the distribution of values in a dataset is overall clustered, dispersed, or random. Meanwhile, local Moran's I is a per-feature measure of the similarity of its attribute value with only its own neighbors. As the name suggests, this value varies across a whole given dataset.
2. The typical criteria for deeming a spatial unit a "hotspot" or "coldspot" is that a) their local Moran's I is positive or negative (respectively), and that b) the p-value is below a given threshold (in our case, 0.05). These criteria signify that the spatial unit, which may have a high or low attribute value, is surrounded by neighbors which also have high or low values.
3. The three biggest hotspots are in the western, eastern, and central-southern portions of the AOI. The western and eastern portions are essentially rows of high-value residential parcels, while the south is a large parcel ringed by medium-sized ones that extend to the center. 
4. The single biggest major coldspot is the whole western edge of the AOI, which correspond roughly to the buffer zone and nearby residential areas. 
5. Hotspot islands also appear in the far southeastern corner, as well as just to the northeast of the major eastern hotspot. Meanwhile, some road parcels near hotspots are also deemed coldspots by the local Moran's I analysis.
6. Using KNN or distance-based weighting results in the western edge no longer becoming a coldspot. Instead, small coldspots pop up across the eastern edge of the AOI. Meanwhile, the western and eastern hotspots remain, while the southern hotspot disappears.
7. Only minor changes to the local Moran's I pattern occur when changing the attribute from `"ass_ass_va"` to `"ass_market"`. More small hotspots and coldspots appear in the southeastern portion, while some road coldspots disappear. This makes sense, as while there may be small differences in the spatial distribution of these two attributes (related to assessed parcel value), the overall pattern seem to be the same.