from flask import Flask, render_template, request
# import inspect
app = Flask(__name__)


def convert_to_listcomprehension(outStr):
    # outStr = inspect.getsource(fun)
    dump = []
    out = ""
    result = ""
    mainList = ''
    fetchListName = ''
    for o in outStr.splitlines():
        # print(o.strip())
        ot = o.strip()
        dump.append(ot)
        if('.append' in ot):
            result = f'{ot.split(".")[0]}'
        elif(ot.startswith('for')):
            first = ot.split(' ')[1]
            fetchListName = (ot.split(' ')[3])[:-1]
            out = f"{first} {ot[:-1]}"
            # out2 = f" if color =='red' "
            # out = f"[{first} {ot[:-1]}]"
            # colors = eval(out)
        elif(ot.startswith('if')):
            out += f" {ot.strip()[:-1]}"
            # out += out2[:-1]
    for d in dump:
        # print("result:", mainList)
        if d.startswith(fetchListName):
            mainList = d
        # mainList = d.split('=')[1]
    outputting = f'''
{mainList}
{result} = [{out}]
print({result})
                '''
    # return f'{result} = [{out}]'
    return outputting


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        context = request.form.get('input_func')
        ctx = str(context)
        context2 = convert_to_listcomprehension(context)
        return render_template('index.html', context=context2, ctx=ctx)
    else:
        return render_template('index.html')


# def test():
#     for color in colors:
#         if color == 'red':
#             new_colors.append(color)


# if __name__ == '__main__':
#     app.run(debug=False)
