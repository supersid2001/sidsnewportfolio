from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Game data
data = {
    "1": {
        "id": "1",
        "Name": "Blade and Sorcery",
	    "Platform": "VR",
        "image": "https://cdn.akamai.steamstatic.com/steam/apps/629730/header.jpg?t=1701774481",
	    "Genres": ["Action", "Fantasy"],
	    "Release_Date": 2018,
        "Summary": "Blade and Sorcery is a VR medieval fantasy game known for its realistic physics-based combat system. Players can engage in close combat, archery, and magic to fight enemies in a sandbox environment. The game emphasizes player skill and physical movement, offering a variety of weapons and magical abilities to experiment with in immersive, detailed settings.",
	    "IGN_Score": 8.6,
	    "Steam_Score": 10,
	    "Purchase_Link": "https://store.steampowered.com/app/629730/Blade_and_Sorcery/",
	    "Similar_Game_ids": [2]

    },
    "2": {
        "id": "2",
        "Name": "Batman: Arkham Knight",
	    "Platform": "PC",
        "image": "https://cdn.akamai.steamstatic.com/steam/apps/208650/header.jpg?t=1702934528",
	    "Genres": ["Action", "Superhero"],
	    "Release_Date": 2015,
        "Summary": "Batman™: Arkham Knight brings the award-winning Arkham trilogy from Rocksteady Studios to its epic conclusion. Developed exclusively for New-Gen platforms, Batman: Arkham Knight introduces Rocksteady's uniquely designed version of the Batmobile. The highly anticipated addition of this legendary vehicle, combined with the acclaimed gameplay of the Arkham series, offers gamers the ultimate and complete Batman experience as they tear through the streets and soar across the skyline of the entirety of Gotham City. In this explosive finale, Batman faces the ultimate threat against the city that he is sworn to protect, as Scarecrow returns to unite the super criminals of Gotham and destroy the Batman forever.",
	    "IGN_Score": 9.0,
	    "Steam_Score": 9.5,
	    "Purchase_Link": "https://store.steampowered.com/app/208650/Batman_Arkham_Knight/",
	    "Similar_Game_ids": [1]
    },
    "3": {
        "id": "3",
        "Name": "Stardew Valley",
	    "Platform": "PC",
        "image": "https://cdn.akamai.steamstatic.com/steam/apps/413150/header.jpg?t=1666917466",
	    "Genres": ["Casual", "Simulator", "Builder"],
	    "Release_Date": 2016,
        "Summary": "You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home? It won't be easy. Ever since Joja Corporation came to town, the old ways of life have all but disappeared. The community center, once the town's most vibrant hub of activity, now lies in shambles. But the valley seems full of opportunity. With a little dedication, you might just be the one to restore Stardew Valley to greatness!",
	    "IGN_Score": 9.5,
	    "Steam_Score": 9.7,
	    "Purchase_Link": "https://store.steampowered.com/app/413150/Stardew_Valley/",
	    "Similar_Game_ids": [4]
    },
    "4": {
        "id": "4",
        "Name": "House Flipper",
	    "Platform": "PC",
        "image": "https://cdn.akamai.steamstatic.com/steam/apps/613100/header.jpg?t=1708006378",
	    "Genres": ["Casual", "Builder"],
	    "Release_Date": 2017,
        "Summary": "House Flipper is a unique chance to become a one-man renovation crew. Buy, repair and remodel devastated houses. Give them a second life and sell them at a profit!",
	    "IGN_Score": 8.5,
	    "Steam_Score": 9.6,
	    "Purchase_Link": "https://store.steampowered.com/app/613100/House_Flipper/",
	    "Similar_Game_ids": [3]
    },
    "5": {
        "id": "5",
        "Name": "Batman: Arkham City",
	    "Platform": "PC",
        "image": "https://cdn.akamai.steamstatic.com/steam/apps/200260/header.jpg?t=1702934622",
	    "Genres": ["Action", "Superhero"],
	    "Release_Date": 2012,
        "Summary": "Batman: Arkham City builds upon the intense, atmospheric foundation of Batman: Arkham Asylum, sending players flying through the expansive Arkham City - five times larger than the game world in Batman: Arkham Asylum - the new maximum security home for all of Gotham City's thugs, gangsters and insane criminal masterminds. Featuring an incredible Rogues Gallery of Gotham City's most dangerous criminals including Catwoman, The Joker, The Riddler, Two-Face, Harley Quinn, The Penguin, Mr. Freeze and many others, the game allows players to genuinely experience what it feels like to be The Dark Knight delivering justice on the streets of Gotham City.",
	    "IGN_Score": 9.5,
	    "Steam_Score": 9.5,
	    "Purchase_Link": "https://store.steampowered.com/app/200260/Batman_Arkham_City__Game_of_the_Year_Edition/",
	    "Similar_Game_ids": [2, 1]
    }
}

@app.route('/')
def home():
    # Pass first 3 items to "Popular items"
    popular_items = [data[item] for item in data][:3]
    return render_template('home.html', items=popular_items)

from flask import Flask, request, render_template, jsonify, redirect, url_for

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_id = str(len(data) + 1)  
        
        # Process form data and validation here as needed
        item = {
            'id': new_id,
            'Name': request.form.get('Name'),
            'Platform': request.form.get('Platform'),
            'Genres': request.form.get('Genres').split(', '),  # Split genres by comma
            'Release_Date': int(request.form.get('Release_Date')),
            'Summary': request.form.get('Summary'),
            'IGN_Score': float(request.form.get('IGN_Score')),
            'Steam_Score': float(request.form.get('Steam_Score')),
            'Purchase_Link': request.form.get('Purchase_Link'),
            "image": request.form.get('Image_Link'),
        }

        data[new_id] = item 

        # Return a JSON response indicating success and the new item's ID
        return jsonify({'success': True, 'newItemId': new_id})
    
    return render_template('add_item.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_item(id):
    game = data.get(id)
    if not game:
        return "Game not found", 404

    if request.method == 'POST':
        # Processing the form data submitted via POST request
        genres_str = request.form.get('Genres', '')
        genres_list = [genre.strip() for genre in genres_str.split(',')] if genres_str else []

        # Construct updated information dictionary
        updated_info = {
            'Name': request.form.get('Name', game['Name']),  
            'Platform': request.form.get('Platform', game['Platform']),
            'Genres': genres_list,
            'Release_Date': int(request.form.get('Release_Date', game['Release_Date'])),
            'Summary': request.form.get('Summary', game['Summary']),
            'IGN_Score': float(request.form.get('IGN_Score', game['IGN_Score'])),
            'Steam_Score': float(request.form.get('Steam_Score', game['Steam_Score'])),
            'Purchase_Link': request.form.get('Purchase_Link', game['Purchase_Link']),
            "image": request.form.get('Image_Link'),
        }

        # Update the game information in your data structure
        data[id].update(updated_info)

        return jsonify({'success': True, 'message': 'Item updated successfully'})

    # If it is a GET request, render the form with existing game data
    return render_template('edit_item.html', game=game)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip() 
    if not query:
        return redirect(url_for('home'))

    # Perform a case-insensitive substring search across multiple fields
    results = {key: value for key, value in data.items() if query.lower() in value['Name'].lower() or
               any(query.lower() in genre.lower() for genre in value['Genres']) or
               query.lower() in value['Platform'].lower()}

    feedback_msg = f"{len(results)} results found for \"{query}\"." if results else "No matches found."
    
    return render_template('search.html', query=query, results=results, feedback_msg=feedback_msg)

@app.route('/view/<id>')
def view(id):
    item = data.get(id)
    if item:
        return render_template('view.html', item=item)
    # Error if item not there
    else:
        return 'Item not found', 404

if __name__ == '__main__':
    app.run(debug=True)