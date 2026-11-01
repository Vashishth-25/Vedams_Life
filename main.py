from flask import Flask, render_template, request, redirect, url_for, send_file


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route('/levels')
def levels():
    return render_template('levels.html')
    # return send_file('static/bgm1.mp3', mimetype='audio/mp3')

@app.route('/lvl_1')
def lvl_1():
    return render_template('all_levels/lvl_1.html')

@app.route('/lvl_2')
def lvl_2():
    return render_template('all_levels/lvl_2.html')

@app.route('/lvl_3')
def lvl_3():
    return render_template('all_levels/lvl_3.html')

@app.route('/lvl_4')
def lvl_4():
    return render_template('all_levels/lvl_4.html')

@app.route('/lvl_5')
def lvl_5():
    return render_template('all_levels/lvl_5.html')





@app.route('/lvl1_lec')
def lvl1_lec():
    return render_template('all_levels/lvl1_lec.html')
@app.route('/lvl2_lec')
def lvl2_lec():
    return render_template('all_levels/lvl2_lec.html')
@app.route('/lvl3_lec')
def lvl3_lec():
    return render_template('all_levels/lvl3_lec.html')
@app.route('/lvl4_lec')
def lvl4_lec():
    return render_template('all_levels/lvl4_lec.html')
@app.route('/lvl5')
def lvl5():
    return render_template('all_levels/lvl_5.html')





@app.route('/lvl1_ques')
def lvl1_ques():
    return render_template('lvl1_ques.html')

@app.route('/lvl2_ques')
def lvl2_ques():
    return render_template('lvl2_ques.html')

@app.route('/lvl3_ques')
def lvl3_ques():
    return render_template('lvl3_ques.html')

@app.route('/lvl4_ques')
def lvl4_ques():
    return render_template('lvl4_ques.html')






@app.route('/play_video', methods=['POST'])
def play_video():
    input_value = request.form['input_value']
    
    if input_value == '342':
        video_path = 'lvl1_yes.mp4'
    else:
        video_path = 'lvl1_no.mp4'
    
    return render_template('play_video.html', video_path=video_path)

@app.route('/play_video_2', methods=['POST'])
def play_video_2():
    input_value = request.form['input_value']
    
    if input_value == '45':
        video_path = 'lvl2_yes.mp4'
    else:
        video_path = 'lvl2_no.mp4'
    
    return render_template('play_video_2.html', video_path=video_path)

@app.route('/play_video_3', methods=['POST'])
def play_video_3():
    input_value = request.form['input_value']
    
    if input_value == '3, -2' or "-2, 3":
        video_path = 'lvl3_yes.mp4'
    else:
        video_path = 'lvl3_no.mp4'
    
    return render_template('play_video_3.html', video_path=video_path)

@app.route('/play_video_4', methods=['POST'])
def play_video_4():
    input_value = request.form['input_value']
    
    if input_value == 'Maternal Uncle':
        video_path = 'lvl4_yes.mp4'
    else:
        video_path = 'lvl4_no.mp4'
    
    return render_template('play_video_4.html', video_path=video_path)



@app.route('/retry1')
def retry1_page():
    return render_template('retry1.html')
@app.route('/retry2')
def retry2_page():
    return render_template('retry2.html')
@app.route('/retry3')
def retry3_page():
    return render_template('retry3.html')
@app.route('/retry4')
def retry4_page():
    return render_template('retry4.html')
@app.route('/retry5')
def retry5_page():
    return render_template('retry5.html')




if __name__ == "__main__":
    app.run(debug = True)

