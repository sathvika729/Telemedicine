from flask import Flask, request, render_template,jsonify,url_for

app = Flask(__name__)
# sample login and passwords
users={"radhika":"r123","priya":"p123","sathvika":"s123","lavanya":"l123","vasudha":"v123"}

# sample doctors data
doctors_data={"Chittoor":{"General Physician":[{"name":"Dr. Ram","id":1},{"name":"Dr. Janu","id":2}],"Cardiology":[{"name":"Dr. Pratap","id":3},{"name":"Dr. Ramya","id":4}],"Orthopedic":[{"name":"Dr. John","id":5},{"name":"Dr. Sowmya","id":6}],"ENT":[{"name":"Dr. Somu","id":7},{"name":"Dr. Danya","id":8}]},
              "Tirupati":{"General Physician":[{"name":"Dr. Geeta","id":9},{"name":"Dr. Ajay","id":10}],"Cardiology":[{"name":"Dr. Varshini","id":11},{"name":"Dr.Rahul","id":12}],"Orthopedic":[{"name":"Dr. Jay","id":13},{"name":"Dr. Jaya","id":14}],"ENT":[{"name":"Dr. Govind","id":15},{"name":"Dr. Priya","id":16}]},
              "Chandragiri":{"General Physician":[{"name":"Dr. Seeta","id":17},{"name":"Dr. Raj","id":18}],"Cardiology":[{"name":"Dr. Satish","id":19},{"name":"Dr. Sadana","id":20}],"Orthopedic":[{"name":"Dr. Stephen","id":21},{"name":"Dr. Sushma","id":22}],"ENT":[{"name":"Dr. Mery","id":23},{"name": "Dr. Ali","id":24}]},
              "Vellore":{"General Physician":[{"name":"Dr. Yamini","id":25},{"name":"Dr. Sunil","id":26}],"Cardiology":[{"name":"Dr. Bumra","id":27},{"name":"Dr. Anusha","id":28}],"Orthopedic":[{"name":"Dr. Srinu","id":29},{"name":"Dr. Sanvi","id":30}],"ENT":[{"name":"Dr. Vijay","id":31},{"name":"Dr. Lakshmi","id":32}],},}

    
@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template('Login.html')
    elif request.method=="POST":
        name=request.form.get("un")
        password=request.form.get("pwd")
        opwd=users.get(name)
        if opwd==password:
           return render_template('options.html',user=name)
        else:
            return "please check your password"   
@app.route("/decide", methods=['POST'])
def handle_option():
    option=request.form.get("one") 
    if option=="appointment":
        return render_template('appointment.html',doctors_data=doctors_data)
    else:
        return "invalid"
@app.route("/go", methods=['POST'])
def handle_go():
    option=request.form.get("two")
    if option=="prescription":
        return render_template('prescription.html')
    else:
        return "choose"
@app.route("/appointment", methods=['POST'])
def appointments():
    if request.method=='POST':
        data = {
        "name": request.form.get("na"),
        "mobile": request.form.get("mn"),
        "location": request.form.get("location"),
        "department": request.form.get("Department"), 
        "doctor_id": request.form.get("Doctor_name"), 
        "slot": request.form.get("Available_slots"),   
        "datetime": request.form.get("date"),       
        "symptoms": request.form.get("symptoms")
        }
    # Find the doctor's name from the ID (optional but good for confirmation)
    doctor_name = "Unknown"
    try:
        loc = data["location"]
        dept = data["department"]
        doc_id = int(data["doctor_id"]) 
        if loc in doctors_data and dept in doctors_data[loc]:
            for doctor in doctors_data[loc][dept]:
                if doctor["id"] == doc_id:
                    doctor_name = doctor["name"]
                    break

    except (KeyError, ValueError, TypeError):
        pass # Handle cases where data might be missing or ID isn't an int


    # Save the appointment (e.g., to a database, file, or just print for now
    print("Appointment Received:")
    print(f"  Name: {data['name']}")
    print(f"  Mobile: {data['mobile']}")
    print(f"  Location: {data['location']}")
    print(f"  Department: {data['department']}")
    print(f"  Doctor ID: {data['doctor_id']} (Name: {doctor_name})")
    print(f"  Slot: {data['slot']}")
    print(f"  Date/Time: {data['datetime']}")
    print(f"  Symptoms: {data['symptoms']}")

    # 3. Return a confirmation message/page to the user
    # You could render a new template: return render_template('confirmation.html', data=data, doctor_name=doctor_name)
    return f"Appointment for {data['name']} with Dr. {doctor_name} ({data['department']} at {data['location']}) submitted successfully for {data['datetime']}! We will contact you at {data['mobile']}."
    
   # --- JSON Endpoint for Doctor Data ---
@app.route("/json")
def doc_data():
    return jsonify(doctors_data)

@app.route("/prescription", methods=['POST'])
def prescr():
    if request.method=='POST':
        patient_data = {
            'fullname': request.form.get('fullname'),
            'dob': request.form.get('dob'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'medications': request.form.get('medications'),
            'allergies': request.form.get('allergies'),
            'conditions': request.form.get('conditions'),
            'surgeries': request.form.get('surgeries'),
            'symptoms': request.form.get('symptoms'),
            'duration': request.form.get('duration'),
            'severity': request.form.get('severity'),
        }
        return render_template('prsction_submit.html', data=patient_data)

    return render_template('prescription.html')

if __name__=='__main__':
    app.run(debug=True) 


        
