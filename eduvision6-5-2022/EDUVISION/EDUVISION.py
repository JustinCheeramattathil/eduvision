from flask import Flask,render_template,request,redirect,session
import random
import datetime
from DBConnection import Db

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
                return redirect('/Admin')
            elif qry['utype']=='PARENT':
                session['s_id']=qry['login_id']
                return redirect('/parent')
                # ss = db.select("select * from parent,pta_members where parent.parent_id=pta_members.member_id and pta_members.member_id='"+str(session['s_id'])+"' ")
                # res = db.select("select * from parent,pta_members where parent.parent_id=pta_members.member_id and pta_members.member_id='" + str(session['s_id']) + "' and pta_members.position='president'")
                # print(session['s_id'])

                # return render_template('PARENT/parent.html',data=ss,data1=res)
            elif qry['utype']=='TEACHERS':
                return  redirect('/TEACHERS')
            else:
                return '''<script>alert('user not found');window.location="/"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''


    else:
        return render_template("login.html")
@app.route('/Admin')
def Admin():

        return render_template("Admin/admin_index.html")

@app.route('/add_exam',methods=['GET','POST'])
def add_exam():
    if request.method=='POST':
        examdate=request.form['textfield']
        examtime=request.form['textfield2']
        course=request.form['select']
        subject=request.form['select2']
        db=Db()
        db.insert("insert into examscheduling VALUES ('','"+examdate+"','"+examtime+"','"+course+"','"+subject+"')")
        return '<script> alert("exam added");window.location="/Admin"</script>'

    else:
        db = Db()
        qry = db.select("select * from course ")
        qry1 = db.select("select * from subject")

        return render_template("Admin/add_exam.html",data = qry,data1 = qry1)



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

@app.route('/add_managementdecisions',methods=['GET','POST'])
def add_managementdecisions():
    if request.method=='POST':
        title=request.form['textfield2']
        decisions=request.files['fileField2']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        decisions.save(r"C:\Users\thoma\PycharmProjects\EDUVISION\static\dimage\\"+date+'.jpg')
        s="/static/dimage/"+date+'.jpg'
        db=Db()
        qry=db.insert("insert into management_decisions VALUES ('',curdate(),'"+title+"','"+str(s)+"')" )
        print(qry)
        return '<script>alert("management decisions added");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_management decisions.html")

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
    else:

        return render_template("Admin/add_parent.html")















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

        db.update("update parent set parent_name='"+parentname+"',phone='"+phone+"',house='"+housename+"',place='"+place+"',post='"+post+"',pin='"+pin+"',occupation='"+occupation+"',relation_with_student='"+relation_with_student+"'")
        return '<script>alert("parent edited");window.location="/Admin"</script>'
    else:
        db=Db()
        ss=db.selectOne("select * from parent where parent_id='"+str(k)+"'")

        return render_template("Admin/edit_parent.html",data=ss)







@app.route('/view_stud_parent/<s_id>')
def view_stud_parent(s_id):
    qry = "select * from parent where student_id = '"+s_id+"'"
    db = Db()
    res = db.select(qry)
    return render_template("Admin/view_stud_parent.html", res=res)


@app.route('/delete_stud_parent/<p_id>')
def delete_stud_parent(p_id):
    db = Db()
    res = db.delete("delete from parent where parent_id = '"+p_id+"'")
    return '<script>alert("parent deleted");window.location="/Admin"</script>'

# @app.route('/add_parent1')
# def add_parent1():
#     return render_template("Admin/add_parent.html")


# @app.route('/add_ptainfo',methods=['GET','POST'])
# def add_ptainfo():
#     if request.method =='POST':
#         db=Db()
#         c = request.form['select']
#         if c == 'parents':
#             res = db.select("select * from parent")
#             return render_template("Admin/add_ptainfo.html", res=res)
#         if c=='teachers':
#             res=db.select("select * from staff")
#             return render_template("Admin/add_ptainfo.html", res=r)
#         return '<script>alert("PTA added");window.location="/Admin"</script>'
#     else:
#         db = Db()
#         qry = "select * from parent"
#         qry1="select * from staff"
#         res = db.select(qry)
#         r=db.select(qry1)
#         return render_template("Admin/add_ptainfo.html")


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



@app.route('/add_rules',methods=['GET','POST'])
def add_rules():
    if request.method=='POST':
        rules= request.form['textarea']
        db=Db()
        db.insert("insert into institutionrules VALUES ('','"+rules+"',curdate())")
        return '<script>alert("rules added");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_rules.html")



@app.route('/add_staffinfo',methods=['GET','POST'])
def add_staffinfo():
    if request.method=='POST':
        staff_name=request.form['textfield']
        department=request.form['textfield2']
        email=request.form['textfield3']
        phone=request.form['textfield4']
        qualification=request.form['textarea']
        house=request.form['textarea2']
        place=request.form['textfield5']
        pin=request.form['textfield6']
        post= request.form['textfield7']
        password = random.randint(0000, 9999)
        db=Db()
        qry = db.insert("insert into login VALUES('','" + email + "','" + str(password) + "','staff')")
        print(staff_name,department,email,phone,qualification,house,place,pin,post)
        db.insert("insert into staff VALUES('"+str(qry)+"','"+staff_name+"','"+department+"','"+email+"','"+phone+"','"+qualification+"','"+house+"','"+place+"','"+pin+"','"+post+"')")
        return '<script>alert("staff added");window.location="/Admin"</script>'
    else:
        return render_template("Admin/add_staffinfo.html")

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
        return '<script>alert("student added");window.location="/add_parent"</script>'
    else:
        db=Db()
        q=db.select("select * from course")
        return render_template("Admin/add_student.html",d=q)

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

@app.route('/add_student')
def add_student():

    return render_template("Admin/add_student.html")

@app.route('/view_complaints')
def view_complaints():
    qry="select * from complaint,parent where complaint.parent_id=parent.parent_id and complaint.reply='pending'"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_complaints.html",data=res)

@app.route('/send_reply/<a>',methods=['get','post'])
def send_reply(a):
    if request.method=="POST":
        reply=request.form['textarea']
        db=Db()
        db.update("update complaint set reply='"+reply+"',reply_date=curdate() where complaintid='"+a+"'")
        return '<script>alert("reply added");window.location="send_reply"</script>'
    else:
        return render_template("Admin/send_reply.html")


@app.route('/view_exam')
def view_exam():
    qry = "select * from examscheduling,course,subject WHERE examscheduling.course_id=course.course_id AND examscheduling.subject_id=subject.subject_id"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_exam.html",res=res)

@app.route('/examdelete/<i>')
def examdelete(i):
    db=Db()
    db.delete("delete from examscheduling where exam_id='"+i+"'")
    return redirect('/view_exam')

@app.route('/editexam/<c>',methods=['get','post'])
def editexam(c):
    if request.method=="POST":

        pa=request.form['textfield']
        du=request.form['textfield2']
        se=request.form['select2']
        ed=request.form['select3']

        db=Db()
        q=db.update("update examscheduling set examdate='"+pa+"', examtime='"+du+"',course_id='"+se+"',subject_id='"+ed+"' where exam_id='"+str(c)+"' ")
        print(q)
        return view_exam()
    else:
        db=Db()
        qry = db.select("select * from course ")
        qry1 = db.select("select * from subject")
        q=db.selectOne("select * from examscheduling WHERE exam_id='"+str(c)+"'")
        return render_template("Admin/edit_exam.html",res=q,res1=qry1,data=qry)



@app.route('/view_fine')
def view_fine():
    qry = "select * from fine,student WHERE fine.stud_id=student.stud_id "
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_fine.html",res=res)


@app.route('/edit_fine/<i>',methods=['get','post'])
def editfine(i):
    if request.method=="POST":
        std=request.form['stud']
        pa=request.form['textarea1']
        du=request.form['textfield4']
        db=Db()
        q=db.update("update fine set date=curdate(), penaltyreason='"+pa+"',due_amount='"+du+"',stud_id='"+std+"' where fineid='"+i+"' ")
        print(q)
        return view_fine()
    db=Db()
    q=db.selectOne("select * from fine,student WHERE fine.stud_id=student.stud_id and fineid='"+i+"'")
    q1=db.select("select * from student")
    return render_template("Admin/update_fine.html",data=q,d=q1)


@app.route('/view_managementdecisions')
def view_managementdecisions():
    qry="select * from management_decisions "
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_managementdecisions.html",res=res)





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
        du.save(r"C:\Users\thoma\PycharmProjects\EDUVISION\static\dimage\\" + date + '.jpg')
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





@app.route('/view_parent')
def view_parent():
    qry="select * from parent,student WHERE parent.student_id=student.stud_id "
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_parent.html",res=res)


@app.route('/parents_delete/<p_id>')
def parentsdelete(p_id):
    db=Db()
    db.delete("delete from parent where parent_id='"+p_id+"'")
    return redirect('/view_parent')



@app.route('/add_pta_position/<p_id>',methods=['GET','POST'])
def add_pta_position(p_id):
    if request.method=="POST":
        position = request.form['textfield']
        db=Db()
        db.insert("insert into pta_members values('','"+p_id+"','"+position+"')")
        return '<script>alert("ok");window.location="/Admin"</script>'

    else:
        db=Db()
        db.select
        return render_template('Admin/pta_position.html')

# @app.route('/add_parent_pta/')
# def addparentpta(i):
#     return '<script>alert("Added as pta");window.location="/Admin"</script>'





#@app.route('/view_pta')
# def view_pta():
#     qry="select * from pta_members"
#     db=Db()
#     res=db.select(qry)
#     return render_template("Admin/view_pta.html")

@app.route('/view_ptainfo')
def view_ptainfo():
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
    return redirect('/view_ptainfo')

@app.route('/view_rules')
def view_rules():
    qry="select * from institutionrules"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_rules.html",res=res)


@app.route('/view_rulesdelete/<d_id>')
def view_rulesdelete(d_id):
    db=Db()
    db.delete("delete from institutionrules where ruleid='"+d_id+"'")
    return redirect('/view_rules')

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

    qry="select * from notification"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/notifications.html",res=res)


@app.route('/notificationdelete/<n_id>')
def notificationdelete(n_id):
    db=Db()
    db.delete("delete from notification where notification_id='"+n_id+"'")
    return redirect('/view_notification')

@app.route('/view_staffinfo')
def view_staffinfo():
    qry="select * from staff"
    db=Db()
    res=db.select(qry)
    return render_template("Admin/view_staffinfo.html",res=res)

@app.route('/staffinfodelete/<s_id>')
def staffinfodelete(s_id):
    db=Db()
    db.delete("delete from staff where staffid='"+s_id+"'")
    return redirect('/view_staffinfo')

@app.route('/editstaffinfo/<b>',methods=['get','post'])
def editstaffinfo(b):
    if request.method=="POST":

        pa=request.form['textfield']
        du=request.form['textfield2']
        se=request.form['textfield3']
        ed=request.form['textfield4']
        er=request.form['textarea']
        ww=request.form['textarea2']
        eq=request.form['textfield5']
        xc= request.form['textfield6']
        zx= request.form['textfield7']
        db=Db()
        q=db.update("update staff set staff_name='"+pa+"', department='"+du+"',email='"+se+"',phone='"+ed+"',qualification='"+er+"',house='"+ww+"',place='"+eq+"',post='"+xc+"',pin='"+zx+"' where staffid='"+str(b)+"' ")
        print(q)
        return view_staffinfo()
    else:
        db=Db()
        q=db.selectOne("select * from staff WHERE staffid='"+str(b)+"'")
        return render_template("Admin/edit_staffinfo.html",res=q)





@app.route('/add_pta_position1/<sf_id>',methods=['get','post'])
def add_pta_position1(sf_id):
    if request.method=="POST":
        position = request.form['textfield']
        db=Db()
        db.insert("insert into pta_members values('','"+sf_id+"','staff','"+position+"')")
        return '<script>alert("ok");window.location="/Admin"</script>'

    else:
        return render_template('Admin/pta_position1.html')



@app.route('/view_student1')
def view_student():
    qry = "select * from student,course where course.course_id=student.course_id"
    db = Db()
    res=db.select(qry)
    return render_template("Admin/view_student.html",res=res)

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



# ----------------------------------------------teachers-----------------------------------------------------------------------------------------------

# @app.route('/add_PTA_notification',methods=['GET','POST'])
# def add_PTA_notification():
#     if request.method=='POST':
#         type=request.form['select']
#         notification=request.form['textarea']
#         db=Db()
#         qry=db.insert("insert into notification VALUES ('','"+type+"','"+notification+"',curdate())")
#         return '''<script>alert('success');window.location="/PTA"</script>'''
#     else:
#         return render_template("PTA/add_PTA_notification.html")
#
#
#
# @app.route('/view_PTA_notification')
# def view_PTA_notification():
#     qry="select * from notification"
#     db=Db()
#     res=db.select(qry)
#     return render_template("PTA/view_PTA_notification.html",res=res)
#
# @app.route('/view_PTA_notificationdelete/<n_id>')
# def view_PTA_notificationdelete(n_id):
#     db=Db()
#     db.delete("delete from notification where ruleid='"+n_id+"'")
#     return redirect('/
@app.route('/parent')
def parent():

    return render_template("parent/parent.html")







@app.route('/add_feedback',methods=['get','post'])
def add_feedback():
    if request.method == 'POST':
        feedback=request.form['textarea']
        db = Db()
        db.insert("insert into feedback VALUES ('',curdate(),'"+str(session['s_id'])+"','"+feedback+"')")
        return '<script>alert("feedback added");window.location="/parent"</script>'
    else:
        return render_template("parent/add_feedback.html")


@app.route('/ADD_COMPLAINT',methods=['GET','POST'])
def ADD_COMPLAINT():
    if request.method=='POST':
        complaint=request.form['textarea']
        db = Db()
        db.insert("insert into complaint VALUES ('',curdate(),'"+str(session['s_id'])+"','"+complaint+"','pending','pending')")
        return '<script>alert("complaints reported");window.location="/parent"</script>'
    else:

        return render_template("parent/ADD_COMPLAINT.html")



@app.route('/parent_view_ptascheduling')
def parent_view_ptascheduling():
    qry="select * from pta_meeting"
    db=Db()
    res=db.select(qry)
    return render_template("PARENT/view_ptascheduling.html",res=res)


@app.route('/view_academicperformance')
def view_academicperformance():
    qry = "select * from academic_performance"
    db = Db()
    res = db.select(qry)
    return render_template("parent/view_academic performance.html")

@app.route('/view_attendence')
def view_attendence():
    qry = "select * from attendence"
    db = Db()
    res = db.select(qry)
    return render_template("parent/view_attendence.html")

@app.route('/VIEW_COMPLAINT')
def view_compliant():
    qry = "select * from complaint"
    db = Db()
    res = db.select(qry)
    return render_template("parent/VIEW_COMPLAINT.html",res=res)


@app.route('/view_feedback')
def view_feedback():
    qry="select * from feedback where feedback.parent_id='"+str(session['s_id'])+"'"
    db=Db()
    res=db.select(qry)
    return render_template("parent/view_feedback.html",data=res)

@app.route('/view_marks')
def view_marks():
    return render_template("parent/view_marks.html")

@app.route('/view_management_responses_parent')
def view_management_responses_parent():
    return render_template("parent/management responses.html")

@app.route('/view_fine1')
def view_fine1():
    return render_template("parent/view_fine1.html")

@app.route('/view_NOTIFICATION_CORNER')
def view_NOTIFICATION_CORNER():
    return render_template("parent/NOTIFICATION CORNER.html")

@app.route('/add_PTAnotification')
def add_PTAnotification():
    return render_template("parent/add_PTAnotification.html")

@app.route('/view_PTAnotification')
def view_PTAnotification():
    return render_template("parent/view_PTAnotification.html")

@app.route('/view_ptamembers')
def view_ptamembers():
    return render_template("parent/view_ptamembers.html")

@app.route('/a')
def a():
    return render_template("Admin/admin_index.html")



@app.route('/parent_view_rules')
def parent_view_rules():
    qry="select * from institutionrules"
    db=Db()
    res=db.select(qry)
    return render_template("PARENT/view_rules.html",res=res)


@app.route('/parent_view_managementdecisions')
def parent_view_managementdecisions():
    qry="select * from management_decisions "
    db=Db()
    res=db.select(qry)
    return render_template("PARENT/view_managementdecisions.html",res=res)



@app.route('/parent_view_notification')
def parent_view_notification():
        db = Db()
        res = db.select("select * from notification where n_type='PARENTS'")
        return render_template("PARENT/view_notifications.html", data=res)



if __name__ == '__main__':
    app.run(port=1000)
