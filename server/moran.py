from esda.moran import Moran, Moran_Local

def calculate_global_morans_I(gdf, weights_obj, attribute):
    y = gdf[attribute].values
    moran = Moran(y, weights_obj)

    return moran.I, moran.p_sim

def calculate_local_morans_I(gdf, weights_obj, attribute):
    y = gdf[attribute].values
    local = Moran_Local(y, weights_obj)

    gdf["local_I"] = local.Is
    gdf["p_value"] = local.p_sim
    gdf["cluster"] = "Not Significant"

    gdf.loc[(gdf["local_I"] > 0) & (gdf["p_value"] < 0.05), "cluster"] = "Hotspot"
    gdf.loc[(gdf["local_I"] < 0) & (gdf["p_value"] < 0.05), "cluster"] = "Coldspot"

    return gdf