def crop(crop_name):
    crop_data = {
    "wheat":["https://cdn.pixabay.com/photo/2015/02/18/16/10/wheat-field-640960_960_720.jpg", "U.P., Punjab, Haryana, Rajasthan, M.P., bihar", "rabi"],
    "paddy":["https://cdn.pixabay.com/photo/2014/10/22/18/43/rice-498688_960_720.jpg", "W.B., U.P., Andhra Pradesh, Punjab, T.N.", "kharif"],
    "barley":["https://cdn.pixabay.com/photo/2014/06/20/19/36/barley-373360_960_720.jpg", "Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "rabi"],
    "maize":["https://cdn.pixabay.com/photo/2014/03/25/16/23/corn-296956_960_720.png", "Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "kharif"],
    "bajra":["https://cdn.pixabay.com/photo/2013/11/01/18/21/pearl-millet-204098_960_720.jpg", "Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "kharif"],
    "copra":["https://cdn.pixabay.com/photo/2016/07/06/20/56/coconut-1501334_960_720.jpg", "Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, Orissa, West Bengal", ""],
    "cotton":["https://cdn.pixabay.com/photo/2013/04/03/12/31/clematis-vitalba-99887_960_720.jpg", "Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", ""],
    "masoor":["https://cdn.pixabay.com/photo/2016/08/28/22/07/sesame-1627005_960_720.jpg", "Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal, Rajasthan", "rabi"],
    "gram":["https://cdn.pixabay.com/photo/2013/07/25/11/56/channa-166896_960_720.jpg", "Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka","rabi"],
    "groundnut":["https://cdn.pixabay.com/photo/2018/01/02/07/22/food-3055647_960_720.jpg", "Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "kharif"],
    "arhar":["https://cdn.pixabay.com/photo/2018/12/14/08/33/pigeon-peas-3874445_960_720.jpg", "Maharashtra, Karnataka, Madhya Pradesh and Andhra Pradesh", "kharif"],
    "sesamum":["https://cdn.pixabay.com/photo/2014/04/05/11/39/sesame-316590_960_720.jpg", "Maharashtra, Rajasthan, West Bengal, Andhra Pradesh, Gujarat", "rabi"],
    "jowar":["https://cdn.pixabay.com/photo/2018/08/22/22/46/field-3624849_960_720.jpg", "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "kharif"],
    "moong":["https://cdn.pixabay.com/photo/2013/07/25/12/03/chana-166987_960_720.jpg", "Rajasthan, Maharashtra, Andhra Pradesh", "rabi"],
    "niger":["https://cdn.pixabay.com/photo/2016/11/19/15/27/bird-1839844_960_720.jpg", "Andha Pradesh, Assam, Chattisgarh, Gujarat, Jharkhand", "kharif"],
    "rape":["https://cdn.pixabay.com/photo/2013/12/20/14/01/mustard-231302_960_720.jpg", "Rajasthan, Uttar Pradesh, Haryana, Madhya Pradesh, and Gujarat", "rabi"],
    "jute":["https://cdn.pixabay.com/photo/2018/01/25/19/48/pepper-3106925_960_720.jpg", " West Bengal , Assam , Orissa , Bihar , Uttar Pradesh", "kharif"],
    "safflower":["https://cdn.pixabay.com/photo/2010/12/13/10/11/safflower-2423_960_720.jpg",  "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Orissa", "kharif"],
    "soyabean":["https://cdn.pixabay.com/photo/2015/09/29/18/41/soy-964324_960_720.jpg",  "Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "kharif"],
    "urad":["https://www.boldsky.com/img/2018/12/xcoverimage-1544088609.png.pagespeed.ic.zeG4XwCeHo.jpg",  "Andhra Pradesh, Maharashtra, Madhya Pradesh, Tamil Nadu", "rabi"],
    "ragi":["https://cdn.pixabay.com/photo/2016/09/26/21/18/millet-1697117_960_720.jpg",  "Maharashtra, Tamil Nadu and Uttarakhand", "kharif"],
    "sunflower":["https://cdn.pixabay.com/photo/2018/04/05/14/09/sun-flower-3292932_960_720.jpg",  "Karnataka, Andhra Pradesh, Maharashtra, Bihar, Orissa", "rabi"],
    "sugarcane":["https://cdn.pixabay.com/photo/2014/04/03/11/35/sugarcane-311914_960_720.png","Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh" , "kharif"]
    }
    return crop_data[crop_name]