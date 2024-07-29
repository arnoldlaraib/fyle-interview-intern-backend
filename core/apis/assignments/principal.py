# Example implementation for GET /principal/assignments
@app.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    principal_header = request.headers.get('X-Principal')
    if not principal_header:
        return jsonify({"error": "Unauthorized"}), 401

    # Fetch assignments from the database
    assignments = Assignment.query.all()
    data = [{"id": a.id, "content": a.content, "grade": a.grade,
             "state": a.state, "student_id": a.student_id, "teacher_id": a.teacher_id} for a in assignments]

    return jsonify({"data": data})

# Example implementation for GET /principal/teachers
@app.route('/principal/teachers', methods=['GET'])
def get_principal_teachers():
    principal_header = request.headers.get('X-Principal')
    if not principal_header:
        return jsonify({"error": "Unauthorized"}), 401

    # Fetch teachers from the database
    teachers = Teacher.query.all()
    data = [{"id": t.id, "user_id": t.user_id, "created_at": t.created_at, "updated_at": t.updated_at} for t in teachers]

    return jsonify({"data": data})

# Example implementation for POST /principal/assignments/grade
@app.route('/principal/assignments/grade', methods=['POST'])
def principal_grade_assignment():
    principal_header = request.headers.get('X-Principal')
    if not principal_header:
        return jsonify({"error": "Unauthorized"}), 401

    payload = request.json
    assignment_id = payload.get('id')
    grade = payload.get('grade')

    # Fetch assignment from the database and update grade
    assignment = Assignment.query.get(assignment_id)
    if assignment:
        assignment.grade = grade
        assignment.state = 'GRADED'
        db.session.commit()

        return jsonify({"data": {"id": assignment.id, "content": assignment.content, "grade": assignment.grade,
                                 "state": assignment.state, "student_id": assignment.student_id, "teacher_id": assignment.teacher_id}})
    else:
        return jsonify({"error": "Assignment not found"}), 404
