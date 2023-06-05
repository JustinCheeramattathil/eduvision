from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask,render_template,request,redirect,session
import random
import datetime, demjson
from DBConnection import Db
import smtplib

app = Flask(__name__)
app.secret_key="abc"

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['textfield']
        password=request.form['textfield2']
        print(username,password)
        db=Db()
        qry= db.selectOne("select * from login WHERE username='"+username+"' and password='"+password+"'")
        if qry is not None:
            s_id= qry['login_id']
            print(s_id)
            if qry['utype']=='ADMIN':
                session['log'] = "lo"
                return redirect('/Admin')
            elif qry['utype']=='PARENT':
                session['log'] = "lo"
                session['s_id']=s_id
                return redirect('/parent')


            elif qry['utype']=='TEACHERS':
                session['log'] = "lo"
                return  redirect('/TEACHERS')
            elif qry['utype']=='PTA':
                session['log'] = "lo"
                return redirect('/pta')
            else:
                return '''<script>alert('user not found');window.location="/"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''


    else:
        return render_template("index.html")



@app.route('/logout')
def logout():
    session['log']=""
    return redirect('/')

@app.route('/Admin')
def Admin():
    if session['log'] == "lo":
        return render_template("Admin/admin_index.html")
    else:
        return redirect('/')


@app.route('/add_department',methods=['get','post'])
def add_department():
    if session['log'] == "lo":
        if request.method=="POST":
            dept_name = request.form['textfield']
            db = Db()
            db.insert("insert into department VALUES ('','"+dept_name+"')")
            return '<script>alert("DEPARTMENT ADDED"); window.location="/Admin"</script>'
        else:
            return render_template('Admin/add_department.html')
    else:
        return redirect('/')


@app.route('/view_department')
def view_department():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from department")
        return render_template('Admin/view_department.html',data=res)
    else:
        return redirect('/')

@app.route('/delete_department/<did>')
def delete_department(did):
    if session['log'] == "lo":
        db=Db()
        db.delete("delete from department where dept_id='"+did+"'")
        return redirect('/view_department')
    else:
        return redirect('/')



@app.route('/add_pta_info',methods=['GET','POST'])
def add_pta_info():
    if request.method=="POST":
        m_type = request.form['select']
        if m_type=="teacher":
            db=Db()
            res = db.select(" select * from staff")
            return render_template('Admin/add_ptainfo.html',data=res)
        elif  m_type=="parent":
            db = Db()
            res1 = db.select(" select * from parent")
            return render_template('Admin/add_ptainfo.html', data1=res1)
        else:
            return"invalid type"
    else:
        return render_template('Admin/add_ptainfo.html')

@app.route('/add_pta_information', methods=['GET','POST'])
def add_pta_information():
    if request.method=="POST":
        member_id = request.form['select1']
        position = request.form['textfield']
        print(position,member_id)
        db=Db()
        res = db.selectOne("select * from pta_members where member_id='"+str(member_id)+"'")
        if res is not None:
            return '<script>alert("Member already exist");window.location="/add_pta_info"</script>'
        else:
            db.insert("insert into pta_members values('','"+member_id+"','"+position+"')")
            return '<script>alert("PTA Added");window.location="/add_pta_info"</script>'

    else:
        return render_template('Admin/add_pta_information.html')

@app.route('/add_ptascheduling',methods=['GET','POST'])
def add_ptascheduling():
    if request.method=='POST':
        Meetingdate=request.form['textfield']
        Meetingtime=request.form['textfield2']
        Meetingplace=request.form['textfield3']
        Agenda=request.form['textarea']
        decision_taken=request.form['textarea2']
        db=Db()
        print(Meetingdate,Meetingtime,Meetingplace,Agenda,decision_taken)
        db.insert("insert into pta_meeting VALUES('','"+Meetingdate+"','"+Meetingtime+"','"+Meetingplace+"','"+Agenda+"','"+decision_taken+"')")
        return'<script>alert("schedule added");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_ptascheduling.html")



@app.route('/view_pta_info')
def view_pta_info():
    db=Db()
    qry="select * from parent,pta_members where pta_members.member_id=parent.parent_id "
    qry1="select * from pta_members,staff where pta_members.member_id=staff.staffid "
    res=db.select(qry)
    ss=db.select(qry1)
    return render_template("Admin/view_ptainfo.html",res1=res,data=ss)

@app.route('/pta_members_delete/<m_id>')
def ptainfodelete(m_id):
    db=Db()
    db.delete("delete from pta_members where member_id='"+m_id+"'")
    return redirect('/view_ptab_info')




@app.route('/add_course',methods=['get','post'])
def add_course():
    if request.method=="POST":
        dept_name=request.form['select']
        course_name = request.form['textfield']
        db = Db()
        db.insert("insert into course VALUES ('','"+dept_name+"','"+course_name+"')")
        return '<script>alert("COURSE ADDED"); window.location="/Admin"</script>'
    else:
        db=Db()
        res = db.select("select * from department")
        return render_template('Admin/add_course.html',data=res)


@app.route('/view_course')
def view_course():
    db=Db()
    res=db.select("select * from course,department where course.dept_id=department.dept_id")
    return render_template('Admin/view_course.html',data=res)

@app.route('/delete_course/<cid>')
def delete_course(cid):
    db=Db()
    db.delete("delete from course where course_id='"+cid+"'")
    return redirect('/view_course')


@app.route('/add_subject',methods=['get','post'])
def add_subject():
    if request.method=="POST":
        subject=request.form['textfield']
        semester=request.form['textfield2']
        course_name = request.form['select']
        db = Db()
        db.insert("insert into subject VALUES ('','"+subject+"','"+semester+"','"+course_name+"')")
        return '<script>alert("SUBJECT ADDED"); window.location="/Admin"</script>'
    else:
        db=Db()
        res = db.select("select * from course")
        return render_template('Admin/add_subject.html',data=res)

@app.route('/view_subject',methods=['get','post'])
def view_subject():
    if request.method == "POST":
        ss = request.form['select2']

        db=Db()
        res1 = db.select("select * from course ")
        # w=db.select("select * from subject where courseid='"+ss+"'")
        # print(w)
        # ss1=db.selectOne("select * from subject_allocation where  subject_allocation.course_id='"+ss+"'")
        # print("sldkfgh",ss1)

        # if ss1 :
        #     q=ss1['subject_id']
        #     print("mxkcn"+str(q))
        #     res = db.select("select * from course,subject where subject.courseid=course.course_id and course.course_id='"+ss+"' and subject.subject_id!='" + str(q) + "'")
        #     print(res)
        #     return render_template('Admin/view_subject.html', p=res, data=res1)
        #
        #
        # else:
        res = db.select("select * from course,subject where subject.courseid=course.course_id and course.course_id='" + ss + "'")
        print(res)
        return render_template('Admin/view_subject.html', p=res, data=res1)


    else:
        db=Db()
        res=db.select("select * from course ")
        # s=db.select("select * from course,subject where subject.courseid=course.course_id")
        return render_template('Admin/view_subject.html',data=res)


@app.route('/teacher_allocate/<b>/<sub>',methods=['get','post'])
def teacher_allocate(b,sub):
    if request.method=="POST":
        sub=request.form['t1']
        teacher=request.form['select']
        db=Db()
        db.insert("insert into subject_allocation VALUES ('','"+sub+"','"+teacher+"','"+b+"')")
        return '''<script>alert('allocated');window.location="/view_subject"</script>'''
    else:
        print("ffff",sub)

        db=Db()
        ss=db.selectOne("select * from department,course where course.dept_id=department.dept_id and course.course_id='"+b+"'")
        print(ss)
        d=ss['course_id']
        a=ss['dept_id']
        print("wwwww",a)

        ss1 = db.selectOne("select * from subject_allocation where  subject_allocation.course_id='" + str(d) + "' and subject_id='"+str(sub)+"'")
        if ss1:
            # f=ss1['teacher_id']
            # print(ss1,f)
            # p = db.select("select * from staff where department='" + str(a) + "' and staffid!='"+str(f)+"'")

            return '''<script>alert('alredy assigned');window.location="/view_subject"</script>'''

        else:
            ssw = db.selectOne("select * from subject_allocation,staff where  subject_allocation.course_id='" + str( d) + "' and subject_allocation.teacher_id=staff.staffid ")
            print(ssw)
            if ssw is not None:
                e=ssw['teacher_id']
                # ssw = db.selectOne("select * from subject_allocation,staff where  subject_allocation.course_id='" + str(d) + "' and subject_allocation.teacher_id=staff.staffid ")
                p = db.select("select * from staff where department='" + str(a) + "' and staffid!='"+str(e)+"'")
                return render_template('Admin/subject_allocation.html', data=p, data1=sub)
            else:
                p = db.select("select * from staff where department='" + str(a) + "' ")
                return render_template('Admin/subject_allocation.html', data=p, data1=sub)



@app.route('/view_allocated_teacher')
def view_allocated_teacher():
    db=Db()
    ss=db.select("select * from subject_allocation,subject,staff,course where subject_allocation.course_id=course.course_id and subject_allocation.teacher_id=staff.staffid and subject_allocation.subject_id=subject.subject_id")
    return render_template('Admin/view_allocated_teacher.html',data=ss)

@app.route('/delete_allocated/<b>')
def delete_allocated(b):
    db=Db()
    db.delete("delete from subject_allocation where id='"+b+"'")
    return redirect('/view_allocated_teacher')




@app.route('/delete_subject/<sid>')
def delete_subject(sid):
    db=Db()
    db.delete("delete from subject where subject_id='"+sid+"'")
    return redirect('/view_subject')


@app.route('/add_student1',methods=['GET','POST'])
def add_student1():
    if request.method=='POST':

        firstname=request.form['textfield2']
        lastname=request.form['textfield3']
        course=request.form['select2']
        semesteryear=request.form['textfield5']
        Admissionnumber=request.form['textfield']
        quota=request.form['select']
        dob=request.form['textfield6']
        print(Admissionnumber,firstname,lastname,dob,course,semesteryear,quota)
        db=Db()
        ss=db.insert("insert into student VALUES('','"+firstname+"','"+lastname+"','"+course+"','"+semesteryear+"','"+Admissionnumber+"','"+quota+"','"+dob+"')")
        # print(ss)
        session['s_id']=ss
        # print(session['s_id'])
        return '<script>alert("student added successfully");window.location="/add_parent"</script>'
    else:
        db=Db()
        q=db.select("select * from course")
        return render_template("Admin/add_student.html",d=q)


@app.route('/view_student1')
def view_student1():
    db = Db()
    # qry = "select * from student,course where course.course_id=student.course_id"
    # db = Db()
    # res=db.select(qry)
    res=db.select("select * from student, course where student.course_id=course.course_id")
    return render_template("Admin/view_student.html",data=res)

@app.route('/delete_student/<p_id>')
def delete_student(p_id):
    db = Db()
    db.delete("delete from student where stud_id = '"+p_id+"'")
    return redirect('/view_student')

@app.route('/edit_student/<sid>',methods=['GET','POST'])
def edit_student(sid):
    if request.method=='POST':
        firstname=request.form['textfield2']
        lastname=request.form['textfield3']
        course=request.form['select2']
        semesteryear=request.form['textfield5']
        Admissionnumber=request.form['textfield']
        quota=request.form['select']
        dob=request.form['textfield6']
        db=Db()
        db.update("update student set first_name= '"+firstname+"',last_name= '"+lastname+"',course_id= '"+course+"',semester= '"+semesteryear+"',admission_number= '"+Admissionnumber+"',quota='"+quota+"',dob='"+dob+"'  where stud_id='"+sid+"' ")
        # print(ss)
        # session['s_id']=ss
        # print(session['s_id'])
        return '<script>alert("STUDENT UPDATED");window.location="/view_student"</script>'
    else:
        db=Db()
        q=db.select("select * from course")
        res=db.selectOne("select * from student where stud_id='"+sid+"'")
        return render_template("Admin/edit_student.html",d=q,loop=res)

@app.route('/view_stud_parent/<s_id>')
def view_stud_parent(s_id):
    db=Db()
    res=db.select("select * from parent,student where parent.student_id=student.stud_id and parent.student_id='"+s_id+"' ")
    return render_template("Admin/view_stud_parent.html", data=res)


@app.route('/delete_stud_parent/<p_id>')
def delete_stud_parent(p_id):
    db = Db()
    db.delete("delete from parent where parent_id = '"+p_id+"'")
    return redirect('/view_stud_parent')


@app.route('/add_rules',methods=['GET','POST'])
def add_rules():
    if request.method=='POST':
        rules= request.form['textarea']
        db=Db()
        db.insert("insert into institutionrules VALUES ('','"+rules+"',curdate())")
        return '<script>alert("RULES ADDED");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_rules.html")

@app.route('/view_rules')
def view_rules():
    qry="select * from institutionrules"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_rules.html",res=res)

@app.route('/delete_rules/<d_id>')
def delete_rules(d_id):
    db=Db()
    db.delete("delete from institutionrules where ruleid='"+d_id+"'")
    return redirect('/view_rules')







@app.route('/add_notification',methods=['GET','POST'])
def add_notification():
    if request.method=='POST':
        typee=request.form['select']
        title=request.form['textfield2']
        content=request.form['textarea']
        db=Db()
        qry=db.insert("insert into notification VALUES ('','"+typee+"','"+title+"','"+content+"',curdate())")
        return '''<script>alert('success');window.location="/Admin"</script>'''
    else:
        return render_template("Admin/add_notification.html")

@app.route('/parent_view_notification',methods=['get','post'])
def parent_view_notification():
    if request.method=='POST':
        db = Db()
        c=request.form['select']
        if c=='PTA':
            res = db.select("select * from notification where n_type='PTA'")
            return render_template("Admin/notifications.html", res=res)
        if c == 'TEACHERS':
            res = db.select("select * from notification where n_type='TEACHERS'")
            return render_template("Admin/notifications.html", res=res)
        if c == 'PARENTS':
            res = db.select("select * from notification where n_type='PARENTS'")
            return render_template("Admin/notifications.html", res=res)

    qry="select * from notification"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/notifications.html",res=res)


@app.route('/delete_notification/<n_id>')
def delete_notification(n_id):
    db=Db()
    db.delete("delete from notification where notification_id='"+n_id+"'")
    return redirect('/view_notification')


@app.route('/Admin_view_feedback')
def Admin_view_feedback():
    qry = "select * from feedback,parent WHERE feedback.parent_id=parent.parent_id"
    db = Db()
    data = db.select(qry)
    return render_template("Admin/view_feedback.html", data=data)


@app.route('/add_managementdecisions',methods=['GET','POST'])
def add_managementdecisions():
    if request.method=='POST':
        title=request.form['textfield2']
        decisions=request.files['fileField2']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        decisions.save(r"C:\Users\thoma\Downloads\EDUVISION_aparna\static\dimage\\"+date+'.jpg')
        s="/static/dimage/"+date+'.jpg'
        db=Db()
        qry=db.insert("insert into management_decisions VALUES ('',curdate(),'"+title+"','"+str(s)+"')" )
        print(qry)
        return '<script>alert("management decisions added");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_management decisions.html")

@app.route('/view_managementdecisions')
def view_managementdecisions():
        qry = "select * from management_decisions "
        db = Db()
        res = db.select(qry)
        return render_template("Admin/view_managementdecisions.html", res=res)

@app.route('/management_decisionsdelete/<d_id>')
def managementdecisionsdelete(d_id):
    db=Db()
    db.delete("delete from management_decisions where decisionid='"+d_id+"'")
    return redirect('/view_managementdecisions')

@app.route('/editmanagementdecisions/<h>',methods=['get','post'])
def editmanagementdecisions(h):
    if request.method=="POST":
        pa=request.form['textfield2']
        du=request.files['fileField2']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        du.save(r"C:\Users\HP\Downloads\EDUVISION\static\dimage\\" + date + '.jpg')
        s = "/static/dimage/" + date + '.jpg'
        if request.files is not None:
            if du.filename!="":

                db=Db()
                # q=db.update("update management_decisions set date=curdate(), title='"+pa+"',decision_taken='"+du+"',file='"+s+"' where decisionid='"+h+"' ")
                res=db.update("update management_decisions set title='"+pa+"',date=curdate(),file='"+str(s)+"' where decisionid='"+h+"'")
                # print(q)
                return view_managementdecisions()
            else:


                db=Db()
                # q=db.update("update management_decisions set date=curdate(), title='"+pa+"',decision_taken='"+du+"',file='"+s+"' where decisionid='"+h+"' ")
                res=db.update("update management_decisions set title='"+pa+"',date=curdate() where decisionid='"+h+"'")
                # print(q)
                return view_managementdecisions()
        else:

            db = Db()
            # q=db.update("update management_decisions set date=curdate(), title='"+pa+"',decision_taken='"+du+"',file='"+s+"' where decisionid='"+h+"' ")
            res = db.update("update management_decisions set title='" + pa + "',date=curdate() where decisionid='" + h + "'")
            # print(q)
            return view_managementdecisions()
    else:
        db=Db()
        q=db.selectOne("select * from management_decisions")
        return render_template("Admin/edit_management decisions.html",res=q)




@app.route('/add_fine',methods=['get','post'])
def add_fine():
    if request.method == 'POST':

        penaltyreason = request.form['textarea1']
        student = request.form['stud']
        due_amount = request.form['textfield4']
        db=Db()
        print(penaltyreason,due_amount)
        db.insert("insert into fine VALUES('',curdate(),'"+penaltyreason+"','"+due_amount+"','"+student+"')")
        return'<script> alert("fine added");window.location="/Admin"</script>'
    else:
        db = Db()
        res = db.select("select * from student")
        return render_template("Admin/add_fine.html",data = res)

@app.route('/view_fine')
def view_fine():
        qry = "select * from fine,student WHERE fine.stud_id=student.stud_id "
        db = Db()
        res = db.select(qry)
        return render_template("Admin/view_fine.html", res=res)

@app.route('/edit_fine/<i>', methods=['get', 'post'])
def editfine(i):
        if request.method == "POST":
            std = request.form['stud']
            pa = request.form['textarea1']
            du = request.form['textfield4']
            db = Db()
            q = db.update("update fine set date=curdate(), penaltyreason='" + pa + "',due_amount='" + du + "',stud_id='" + std + "' where fineid='" + i + "' ")
            print(q)
            return view_fine()
        db = Db()
        q = db.selectOne("select * from fine,student WHERE fine.stud_id=student.stud_id and fineid='" + i + "'")
        q1 = db.select("select * from student")
        return render_template("Admin/update_fine.html", data=q, d=q1)




@app.route('/view_parents_complaints')
def view_parents_complaints():
    db=Db()
    res=db.select("select * from complaint,parent where complaint.parent_id=parent.parent_id and complaint.reply='pending'")
    return render_template("Admin/view_complaints.html",data=res)


@app.route('/admin_send_reply/<cid>',methods=['get','post'])
def admin_send_reply(cid):
    if request.method=="POST":
        reply=request.form['textarea']
        db=Db()
        db.update("update complaint set reply='"+reply+"',reply_date=curdate() where complaintid='"+cid+"' ")
        return '<script>alert("REPLY ADDED");window.location="/view_complaints"</script>'
    else:
        return render_template("Admin/send_reply.html")

@app.route('/add_exam', methods=['GET', 'POST'])
def add_exam():
        if request.method == 'POST':
            examdate = request.form['textfield']
            examtime = request.form['textfield2']
            course = request.form['select']
            subject = request.form['select2']
            db = Db()
            db.insert("insert into examscheduling VALUES ('','" + examdate + "','" + examtime + "','" + course + "','" + subject + "')")
            return '<script> alert("exam added");window.location="/Admin"</script>'

        else:
            db = Db()
            qry = db.select("select * from course ")
            qry1 = db.select("select * from subject")

            return render_template("Admin/add_exam.html", data=qry, data1=qry1)

@app.route('/view_exam')
def view_exam():
            qry = "select * from examscheduling,course,subject WHERE examscheduling.course_id=course.course_id AND examscheduling.subject_id=subject.subject_id"
            db = Db()
            res = db.select(qry)
            return render_template("Admin/view_exam.html", res=res)

@app.route('/examdelete/<i>')
def examdelete(i):
            db = Db()
            db.delete("delete from examscheduling where exam_id='" + i + "'")
            return redirect('/view_exam')

@app.route('/editexam/<c>', methods=['get', 'post'])
def editexam(c):
    if request.method == "POST":
        pa = request.form['textfield']
        du = request.form['textfield2']
        se = request.form['select2']
        ed = request.form['select3']

        db = Db()
        q = db.update("update examscheduling set examdate='" + pa + "', examtime='" + du + "',course_id='" + se + "',subject_id='" + ed + "' where exam_id='" + str(c) + "' ")
        print(q)
        return view_exam()
    else:
        db = Db()
        qry = db.select("select * from course ")
        qry1 = db.select("select * from subject")
        q = db.selectOne("select * from examscheduling WHERE exam_id='" + str(c) + "'")
        return render_template("Admin/edit_exam.html", res=q, res1=qry1, data=qry)


@app.route('/add_staffinfo', methods=['GET', 'POST'])
def add_staffinfo():
        if request.method == 'POST':
            staff_name = request.form['textfield']
            department = request.form['select']
            email = request.form['textfield3']
            phone = request.form['textfield4']
            qualification = request.form['textarea']
            house = request.form['textarea2']
            place = request.form['textfield5']
            pin = request.form['textfield6']
            post = request.form['textfield7']
            password = random.randint(0000, 9999)



            db = Db()
            qry = db.insert("insert into login VALUES('','" + email + "','" + str(password) + "','TEACHER')")
            print(staff_name, department, email, phone, qualification, house, place, pin, post)
            db.insert("insert into staff VALUES('" + str(qry) + "','" + staff_name + "','" + department + "','" + email + "','" + phone + "','" + qualification + "','" + house + "','" + place + "','" + pin + "','" + post + "')")

            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("eduvision12345@gmail.com", "justinthomas1234")
            msg = MIMEMultipart()  # create a message.........."
            msg['From'] = "eduvision12345@gmail.com"
            msg['To'] = email
            msg['Subject'] = "Your Username and Password for Eduvision Website"
            body = "Your username is:- - " + str(email)+"Your Password is:- - " + str(password)
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)


            return '<script>alert("staff added");window.location="/Admin"</script>'
        else:
            db=Db()
            ss=db.select("select * from department")
            return render_template("Admin/add_staffinfo.html",data=ss)

@app.route('/view_staffinfo')
def view_staffinfo():
    qry = "select * from staff"
    db = Db()
    res = db.select(qry)
    return render_template("Admin/view_staffinfo.html", res=res)

@app.route('/staffinfodelete/<s_id>')
def staffinfodelete(s_id):
    db = Db()
    db.delete("delete from staff where staffid='" + s_id + "'")
    return redirect('/view_staffinfo')

@app.route('/editstaffinfo/<b>', methods=['get', 'post'])
def editstaffinfo(b):
    if request.method == "POST":
        pa = request.form['textfield']
        du = request.form['textfield2']
        se = request.form['textfield3']
        ed = request.form['textfield4']
        er = request.form['textarea']
        ww = request.form['textarea2']
        eq = request.form['textfield5']
        xc = request.form['textfield6']
        zx = request.form['textfield7']
        db = Db()
        q = db.update("update staff set staff_name='" + pa + "', department='" + du + "',email='" + se + "',phone='" + ed + "',qualification='" + er + "',house='" + ww + "',place='" + eq + "',post='" + xc + "',pin='" + zx + "' where staffid='" + str(b) + "' ")
        print(q)
        return view_staffinfo()
    else:
        db = Db()
        q = db.selectOne("select * from staff WHERE staffid='" + str(b) + "'")
        return render_template("Admin/edit_staffinfo.html", res=q)




@app.route('/add_parent',methods=['GET','POST'])
def add_parent():
    if request.method=='POST':
        parentname=request.form['textfield']
        housename=request.form['textfield2']
        place=request.form['textfield3']
        phone=request.form['textfield4']
        email=request.form['textfield5']
        post=request.form['textfield6']
        pin=request.form['textfield7']
        occupation=request.form['textfield8']
        relation_with_student =request.form['select']
        password=random.randint(0000,9999)
        db=Db()
        qry=db.insert("insert into login VALUES('','"+email+"','"+str(password)+"','PARENT')")
        s=db.insert("insert into parent VALUES('"+str(qry)+"','"+parentname+"','"+email+"','"+phone+"','"+housename+"','"+place+"','"+post+"','"+pin+"','"+occupation+"','"+relation_with_student+"','"+str(session['s_id'])+"')")
        return '<script>alert("parent added");window.location="/Admin"</script>'




        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("eduvision12345@gmail.com", "justinthomas1234")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "eduvision12345@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Username and Password for Eduvision Website"
        body = "Your username is:- - " + str(email) + "Your Password is:- - " + str(password)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)

        return '<script>alert("parent added");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_parent.html")





@app.route('/view_parent')
def view_parent():
        qry = "select * from parent,student WHERE parent.student_id=student.stud_id "
        db = Db()
        res = db.select(qry)
        return render_template("Admin/view_parent.html", res=res)


@app.route('/parents_delete/<p_id>')
def parentsdelete(p_id):
        db = Db()
        db.delete("delete from parent where parent_id='" + p_id + "'")
        return redirect('/view_parent')


@app.route('/edit_parent/<k>',methods=['GET','POST'])
def edit_parent(k):
    if request.method=='POST':
        parentname=request.form['textfield']
        housename=request.form['textfield2']
        place=request.form['textfield3']
        phone=request.form['textfield4']
        post=request.form['textfield6']
        pin=request.form['textfield7']
        occupation=request.form['textfield8']
        relation_with_student=request.form['select']
        db=Db()
        db.update("update parent set parent_name='"+parentname+"',phone='"+phone+"',house='"+housename+"',place='"+place+"',post='"+post+"',pin='"+pin+"',occupation='"+occupation+"',relation_with_student='"+relation_with_student+"' where parent_id='"+k+"'")
        return '<script>alert("parent edited");window.location="/Admin"</script>'
    else:
        db=Db()
        ss=db.selectOne("select * from parent where parent_id='"+str(k)+"'")

        return render_template("Admin/edit_parent.html",data=ss)


@app.route('/view_notification',methods=['get','post'])
def notification():
    if request.method=='POST':
        db = Db()
        c=request.form['select']
        if c=='PTA':
            res = db.select("select * from notification where n_type='PTA'")
            return render_template("Admin/notifications.html", res=res)
        if c == 'TEACHERS':
            res = db.select("select * from notification where n_type='TEACHERS'")
            return render_template("Admin/notifications.html", res=res)
        if c == 'PARENTS':
            res = db.select("select * from notification where n_type='PARENTS'")
            return render_template("Admin/notifications.html", res=res)

    qry="select * from notification where n_type='PARENTS'"
    db=Db()
    res=db.select(qry)
    return render_template("PARENT/notifications.html",res=res)


@app.route('/notificationdelete/<n_id>')
def notificationdelete(n_id):
    db=Db()
    db.delete("delete from notification where notification_id='"+n_id+"'")
    return redirect('/view_notification')

@app.route('/view_ptascheduling')
def view_ptascheduling():
    qry="select * from pta_meeting"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_ptascheduling.html",res=res)

@app.route('/edit_ptascheduling/<i>',methods=['get','post'])
def editptascheduling(i):
    if request.method=="POST":

        pa=request.form['textfield']
        du=request.form['textfield2']
        se=request.form['textfield3']
        ed=request.form['textarea']
        er=request.form['textarea2']
        db=Db()
        q=db.update("update pta_meeting set meetingdate='"+pa+"', meetingtime='"+du+"',meetingplace='"+se+"',agenda='"+ed+"',decision_taken='"+er+"' where meeting_id='"+str(i)+"' ")
        print(q)
        return view_ptascheduling()
    else:
        db=Db()
        q=db.selectOne("select * from pta_meeting WHERE meeting_id='"+str(i)+"'")
        return render_template("Admin/update_ptascheduling.html",res=q)








# ---------------------------------------------------------------------------------------------------------------------------------------------


# ///////////////////////////////////////////////////////////////////PARENT/////////////////////////////////////////

@app.route('/parent')
def parent():
    db=Db()
    ss = db.select( "select * from parent,pta_members where parent.parent_id=pta_members.member_id and pta_members.member_id='" + str(session['s_id']) + "' ")
    print(ss)
    res = db.select("select * from parent,pta_members where parent.parent_id=pta_members.member_id and pta_members.member_id='" + str( session['s_id']) + "' and pta_members.position='president'")
    print(session['s_id'])

    return render_template('PARENT/parent_index.html', data=ss, data1=res)


@app.route('/view_manager_responses')
def view_manager_responses():
    db=Db()
    res=db.select("select * from management_decisions ")
    return render_template("PARENT/view_responses_of_manager.html",data=res)



@app.route('/add_feedback',methods=['get','post'])
def add_feedback():
    if request.method=="POST":
        feedback=request.form['textarea']
        db=Db()
        db.insert("insert into feedback VALUES ('',curdate(),'"+str(session['s_id'])+"','"+feedback+"')")
        return '<script>alert("FEEDBACK ADDED");window.location="/parent"</script>'
    else:
        return render_template("PARENT/add_feedback.html")


@app.route('/ADD_COMPLAINT',methods=['GET','POST'])
def ADD_COMPLAINT():
    if request.method == 'POST':
        complaint = request.form['textarea']
        db = Db()
        db.insert("insert into complaint VALUES ('',curdate(),'"+str(session['s_id'])+"','"+complaint+"','pending','pending')")
        return '<script>alert("COMPLAINTS REPORTED");window.location="/parent"</script>'
    else:
        return render_template("parent/ADD_COMPLAINT.html")

@app.route('/view_reply')
def view_reply():
        db=Db()
        res=db.select("select * from complaint WHERE complaint.reply!='pending'")
        return render_template('PARENT/view_reply.html', value=res)


@app.route('/view_academic_performance')
def view_academic_performance():
    db=Db()
    res=db.select("select * from academic_performance,student,subject where academic_performance.student_id=student.stud_id and academic_performance.subject_id=subject.subject_id")
    return render_template("parent/view_academic_performancee.html",data=res)



@app.route('/view_attendence')
def view_attendence():
    db=Db()
    res=db.select("select * from attendence,student,staff where attendence.student_id=student.stud_id and attendence.staff_id=staff.staffid")
    return render_template('PARENT/view_attendence.html',data=res)






# @app.route('/send_reply')
# def send_reply():
#     return render_template('')


@app.route('/view_marks')
def view_marks():
    db=Db()
    res=db.select("select * from marks,subject,student where marks.student_id=student.stud_id and marks.subject_id=subject.subject_id")
    return render_template("parent/view_marks.html",data=res)

@app.route('/view_PTAnotification')
def view_PTAnotification():
    db=Db()
    ss=db.select("select * from ptanotification")
    return render_template("parent/view_PTAnotification.html",data=ss)

@app.route('/add_PTAnotification',methods=['get','post'])
def add_PTAnotification():
    if request.method=="POST":
        notification=request.form['textarea']
        db=Db()
        db.insert("insert into ptanotification VALUES ('','"+str(session['s_id'])+"','"+notification+"',curdate())")
        return '''<script>alert('notification send');window.location="/parent"</script>'''
    else:
        return render_template("parent/add_PTAnotification.html")


@app.route('/view_pta_members')
def view_pta_members():
    db=Db()
    # s=db.selectOne("select * from login where login_id='"+str(session['s_id'])+"'")
    # e=s['utype']
    # if s['utype']=='PARENT':
    ss=db.select("select * from parent,pta_members where parent.parent_id=pta_members.member_id ")
    ss1=db.select("select * from pta_members,staff where  staff.staffid=pta_members.member_id ")
    return render_template('PARENT/view_pta_members.html',data=ss,data1=ss1)
    # else:
    #     return '''<script>alert(no data);window.location="/view_pta_members"</script>'''

@app.route('/view_feedback')
def view_feedback():
    qry = "select * from feedback,parent WHERE feedback.parent_id=parent.parent_id"
    db = Db()
    data = db.select(qry)
    return render_template("PARENT/parent_view_feedback.html", data=data)

@app.route('/view_fine1')
def view_fine1():
        qry = "select * from fine,student WHERE fine.stud_id=student.stud_id "
        db = Db()
        res = db.select(qry)
        return render_template("PARENT/view_fine.html", res=res)

# @app.route('/VIEW_COMPLAINT')
# def VIEW_COMPLAINT():
#     qry = "select * from complaint"
#     db = Db()
#     res = db.select(qry)
#     return render_template("PARENT/PARENT_VIEW_COMPLAINT.html",res=res)








# //////////////////////////////////////////////PARENTS CHAT//////////////////////////////////////////////

@app.route('/parent_chat')
def parent_chat():
    # if session['lin'] == "lo":
        # if session['ln'] == "oo":
            return render_template("PARENT/parent_chat.html")
        # else:
        #     return login()
    # else:
    #     return redirect('/')

@app.route('/clg_staff_chat',methods=['post'])
def clg_staff_chat():
    # if session['lin'] == "lo":
        # if session['ln'] == "oo":
            db=Db()
            a=session['s_id']
            q1="select * from staff"
            res = db.select(q1)
            print(res)
            v={}
            if len(res)>0:
                v["status"]="ok"
                v['data']=res
            else:
                v["status"]="error"

            rw=demjson.encode(v)
            print(rw)
            return rw
        # else:
        #     return login()
    # else:
    #     return redirect('/')

@app.route('/chatsnd',methods=['post'])
def chatsnd():
    # if session['lin'] == "lo":
        # if session['ln'] == "oo":
            db=Db()
            c = session['s_id']
            b=request.form['n']
            print(b)
            m=request.form['m']

            q2="insert into chat values(null,'"+str(c)+"','"+str(b)+"','"+m+"',now())"
            res=db.insert(q2)
            v = {}
            if int(res) > 0:
                v["status"] = "ok"

            else:
                v["status"] = "error"

            r = demjson.encode(v)

            return r
        # else:
        #     return login()
    # else:
    #     return redirect('/')

@app.route('/chatrply',methods=['post'])
def chatrply():
    # if session['lin'] == "lo":
        print("...........................")
        c = session['s_id']
        b=request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        return rw
    # else:
    #     return redirect('/')




########################################TEACHER############################


@app.route('/login_teacher',methods=['post'])
def TEACHERS():
    username=request.form['u']
    password=request.form['p']

    print(username,password)
    db=Db()
    ss=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
    res={}
    print(ss)
    print(res)
    if ss:
        db=Db()
        d=ss['login_id']
        print(d)
        dt=db.selectOne("select subject_allocation.subject_id as sid,subject.*,subject_allocation.* from subject,subject_allocation where subject.subject_id=subject_allocation.subject_id and subject_allocation.teacher_id='"+str(d)+"'")
        print(dt)

        if dt is not None:
            print(dt)
            dt1 = db.selectOne("select * from staff WHERE staffid='" + str(d) + "'")
            # q=dt['department']
            print(dt,"jhg")
            res['status']="ok"
            res['type']=ss['utype']
            res['lid']=ss['login_id']
            res['name']=dt1['staff_name']
            res['email']=dt1['email']

            res['cid']=dt['sid']
            # print(res['dtid'])
            return demjson.encode(res)
        else:
            dt1 = db.selectOne("select * from staff WHERE staffid='" + str(d) + "'")
            # q=dt['department']
            print(dt, "jhg")
            res['status'] = "ok"
            res['type'] = ss['utype']
            res['lid'] = ss['login_id']
            res['name'] = dt1['staff_name']
            res['email'] = dt1['email']
            res['cid'] = dt['sid']
            return demjson.encode(res)
        print(res)
    else:
        res['status']=""
        return demjson.encode(res)



@app.route('/view_user_profile',methods=['post'])
def view_user_profile():
    id=request.form['lid']
    db=Db()
    result=db.selectOne("select * from staff where staffid='"+id+"'")
    res={}
    if result:
        res['status']="ok"
        res['data']=result
        return demjson.encode(res)
    else:
        res['status']="none"
        return  demjson.encode(res)


@app.route('/view_students',methods=['post'])
def view_students():
    cid=request.form['cid']
    db=Db()
    ss=db.select("select * from student,course where student.course_id=course.course_id and course.dept_id='"+str(cid)+"' ")

    res={}
    if ss:
        res['status']="ok"
        res['data']=ss
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)

@app.route('/add_performence',methods=['post'])
def add_performence():
    print("hi")
    cid=request.form['cid']
    db=Db()
    ss=db.select("select * from course where dept_id='"+str(cid)+"'")
    ab=db.select("select * from course,subject,subject_allocation where subject_allocation.course_id=course.course_id and subject_allocation.subject_id=subject.subject_id and course.dept_id='"+str(cid)+"'")
    res={}
    if ss :
        res['status']="ok"
        res['data']=ss
        res['data1'] = ab
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)

@app.route('/add_performence_action',methods=['post'])
def add_performence_action():
    stid=request.form['akid']
    subid=request.form['subid']
    arts=request.form['arts']
    sports=request.form['sports']
    studies=request.form['studies']
    cp=request.form['cp']
    interest=request.form['in']
    about=request.form['about']
    lid=request.form['lid']

    db=Db()
    ss=db.insert("insert into academic_performance VALUES ('','"+arts+"','"+sports+"','"+studies+"','"+interest+"','"+about+"','"+cp+"','"+stid+"','"+subid+"',curdate(),'"+lid+"')")

    res={}
    if ss:
        res['status']="ok"
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)


@app.route('/add_mark',methods=['post'])
def add_mark():
    stid=request.form['akid']
    subid = request.form['subid']
    lid = request.form['lid']

    mark=request.form['mark']

    db=Db()
    ss=db.insert("insert into marks VALUES ('','"+stid+"','"+subid+"','"+mark+"','"+lid+"')")

    res={}
    if ss:
        res['status']="ok"
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)

@app.route('/view_mark_teacher',methods=['post'])
def view_mark_teacher():
    akid=request.form['akid']
    lid=request.form['lid']
    db=Db()
    ss=db.selectOne("select * from marks,subject,student where teacher_id='"+lid+"' and student_id='"+akid+"' and marks.subject_id=subject.subject_id and student.stud_id=marks.student_id ")
    print(ss)
    res={}
    if ss:
        res['status']="ok"
        res['data']=ss
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)

@app.route('/view_subject_teacher',methods=['post'])
def view_subject_teacher():
    db = Db()
    ss = db.select("select * from subject")
    res={}
    if ss:
        res['status']="ok"
        res['data']=ss
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)

@app.route('/view_student_teacher',methods=['post'])
def view_student_teacher():
    cid=request.form['cc']
    sid=request.form['ss']
    db = Db()
    ss = db.select("select * from student where course_id='"+cid+"' and semester='"+sid+"'")
    res = {}
    if ss:
        res['status'] = "ok"
        res['data'] = ss
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)


@app.route('/add_attendence', methods=['post'])
def add_attendence():
    stid = request.form['akid']
    lid = request.form['lid']
    radio = request.form['radio']

    db = Db()
    ss = db.insert("insert into attendence VALUES ('',curdate(),'" + stid + "','"+lid+"','" + radio + "')")

    res = {}
    if ss:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)


@app.route('/add_chat',methods=['post'])
def add_chat():
    lid = request.form['lid']
    toid = request.form['toid']
    message = request.form['message']
    db=Db()
    q2="insert into chat values('','"+lid+"','"+toid+"','"+message+"' ,curdate())"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return demjson.encode(res1)

@app.route('/view_chat',methods=['post'])
def view_chat():
    lid = request.form['lid']
    toid = request.form['toid']
    lastid = request.form['lastid']
    print(lid,toid,lastid)
    db=Db()
    q2="select chat.* from chat where chat_id>'"+lastid+"' and ((from_id='"+lid+"' and to_id='"+toid+"') or (from_id='"+toid+"' and to_id='"+lid+"'))"
    res = db.select(q2)
    print(res)
    res1 = {}
    res1['status'] = "ok"
    res1['data'] = res
    return demjson.encode(res1)

@app.route('/view_staff',methods=['post'])
def view_staff():
    lid = request.form['lid']
    cid = request.form['cid']
    print(lid)
    db=Db()

    q = db.select("select * from parent,student,course where parent.student_id=student.stud_id and  student.course_id=course.course_id and course.dept_id='"+str(cid)+"' ")
    # ss = db.select("select * from course where dept_id='" + str(cid) + "'")
    print(q)
    res = {}
    if q:

        res['status'] = "ok"
        res['data'] = q
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)


@app.route('/view_PTAnotification_teacher',methods=['post'])
def view_PTAnotification_teacher():
    db=Db()
    lid=request.form['lid']
    d=db.select("select * from staff,pta_members where staff.staffid=pta_members.member_id and pta_members.member_id='"+lid+"'")
    print(d)
    res = {}
    if len(d)>0:

        ss=db.select("select * from ptanotification")

        if ss:
            res['status']="ok"
            res['data']=ss
            return demjson.encode(res)
        else:
            res['status']=""
            return demjson.encode(res)
    else:

        res['status']=""
        return demjson.encode(res)


@app.route('/view_notification_teacher',methods=['post'])
def view_notification_teacher():
    db=Db()
    qry =db.select( "select * from notification where n_type='TEACHERS'")
    print(qry)
    res={}
    if qry:
        res['status']="ok"
        res['data']=qry
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)



if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0")
