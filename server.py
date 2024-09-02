from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Sample data for Mobile + AR/VR projects
mobile_ar_vr_projects = {
    "1": {
        "id": "1",
        "Name": "Quest2Learn",
        "Platform": "Mobile, AR",
        "image": "Q2L.JPG",
        "Summary": "A collaborative AR educational app developed with JHU students to enhance STEM learning through interactive lab science modules, winning the 2021 DELTA Award.",
        "Technologies": ["Unity", "C#", "Vuforia"],
        "Link": "https://www.youtube.com/watch?v=X1B1jnD45sY"
    },
    "2": {
        "id": "2",
        "Name": "VirtuaLP",
        "Platform": "VR",
        "image": "VirtuaLP.png",
        "Summary": "A VR training system for pediatric lumbar puncture, offering realistic simulations and real-time feedback to improve medical training and procedural accuracy.",
        "Technologies": ["Unity", "C#", "Meta Quest"],
        "Link": "https://youtu.be/UOHfeDaq1sc"
    }
}

# Sample data for Web projects
web_projects = {
    "1": {
        "id": "1",
        "Name": "Wonderful Workouts",
        "Platform": "Web",
        "image": "Wonderful_Workouts.png",
        "Summary": "A small webpage where users get to build their own workout routine and learn new exercises! Built as a final team project UI Design @ Columbia University.",
        "Technologies": ["HTML", "CSS", "JavaScript"],
        "Repo": "https://github.com/supersid2001/Group-2-UI-Design",
        "Link": "https://youtu.be/O4Ypz9iSheA"
    },
    "2": {
        "id": "2",
        "Name": "Video Game Ratings Site",
        "Platform": "Web",
        "image": "Movie_App.png",
        "Summary": "A simple webpage where users can browse and add new video games. Built as my midterm project UI Design @ Columbia University.",
        "Technologies": ["HTML", "CSS", "JavaScript"],
        "Repo": "https://github.com/supersid2001/Games-Repo",
        "Link": "https://youtu.be/YCXrkhMa2QA"
    },
    "3": {
        "id": "2",
        "Name": "Notest",
        "Platform": "Web",
        "image": "Notest.png",
        "Summary": "Notests is a collaborative project with two other JHU students, enhancing e-learning through structured study plans, community sharing, and AI-driven question generation for seamless self-testing.",
        "Technologies": ["React.js", "Next.js", "MongoDB"],
        "Repo": "https://github.com/robertzhidealx/notest",
        "Link": "https://youtu.be/VEOxllDq3tE"
    }
}

# Sample data for Figma prototypes
figma_projects = {
    "1": {
        "id": "1",
        "Name": "Task management application",
        "Platform": "Figma",
        "image": "Task_Figma.png",
        "Summary": "A task management figma project along with a video prototype with personas . Made for the Human-Computer Interaction class @ JHU. ",
        "Technologies": ["Figma"],
        "Link": "https://www.youtube.com/watch?v=5DMYFZ9N028",
        "Repo": "https://www.figma.com/design/JBmOtQ0PwSdk8q7U78l3ZV/HCI-Project-1%3A-Group-3?node-id=0-1&t=inpDTKRi9rkxbG6P-1"
    },
    "2": {
        "id": "2",
        "Name": "Quest2Learn mobile app prototype",
        "Platform": "Web",
        "image": "Q2L_Figma.png",
        "Summary": "Initial Figma prototype built with Quest2Learn team showcasing UI for the Quest2Learn educational mobile application.",
        "Technologies": ["Figma"],
        "Repo": "https://www.figma.com/design/DZlLZPgvzEGFJkk3krRdnz/Quest2Learn-Working-Mockups-(Copy)?node-id=0-1&t=VYyvF0IJJOFlmXt1-1"
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects/mobile-ar-vr')
def mobile_ar_vr():
    return render_template('projects.html', projects=mobile_ar_vr_projects, title="Mobile + AR/VR Projects")

@app.route('/projects/web')
def web_projects_view():
    return render_template('projects.html', projects=web_projects, title="Web Projects")

@app.route('/projects/figma')
def figma_projects_view():
    return render_template('projects.html', projects=figma_projects, title="Figma Prototypes")

@app.route('/view/<id>')
def view(id):
    # Combine all project data into a single dictionary
    combined_data = {**mobile_ar_vr_projects, **web_projects}
    item = combined_data.get(id)
    if item:
        return render_template('view.html', item=item)
    else:
        return 'Item not found', 404

if __name__ == '__main__':
    app.run(debug=True)