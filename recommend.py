from prepare_dataset import prepare_recommendations

def recommend(id):
    recommendations = prepare_recommendations()
    recommend_products = recommendations 
    recommend_products['user_id'] = id 
    column = recommend_products.columns.tolist() 
    column = column[-1:] + column[:-1] 
    recommend_products = recommend_products[column] 
    return recommend_products 

if __name__ == '__main__':
    user_id = 10
    print(recommend(user_id))