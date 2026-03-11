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