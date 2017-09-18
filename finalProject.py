from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, ItemType, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///item.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/item/<int:item_type_id>/menu/JSON')
def itemMenuJSON(item_type_id):
    item = session.query(ItemType).filter_by(id=item_type_id).one()
    items = session.query(MenuItem).filter_by(
        item_type_id=item_type_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/item/<int:item_type_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(item_type_id, menu_id):
    Menu_Item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/item/JSON')
def itemsJSON():
    restaurants = session.query(ItemType).all()
    return jsonify(items=[r.serialize for r in items])


# Show all items
@app.route('/')
@app.route('/item/')
def showItems():
    items = session.query(ItemType).all()
    # return "This page will show all my items"
    return render_template('items.html', items=items)


# Create a new item
@app.route('/item/new/', methods=['GET', 'POST'])
def newItemType():
    if request.method == 'POST':
        newItemType = ItemType(name=request.form['name'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showItems'))
    else:
        return render_template('newItemType.html')
    # return "This page will be for making a new item"

# Edit a item


@app.route('/item/<int:item_type_id>/edit/', methods=['GET', 'POST'])
def editItemType(item_type_id):
    editedItem = session.query(
        ItemType).filter_by(id=item_type_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
            return redirect(url_for('showItems'))
    else:
        return render_template(
            'editItemType.html', item=editedItemType)

    # return 'This page will be for editing item %s' % item_id

# Delete a item


@app.route('/item/<int:item_type_id>/delete/', methods=['GET', 'POST'])
def deleteItemType(item_type_id):
    itemTypeToDelete = session.query(
        ItemType).filter_by(id=item_type_id).one()
    if request.method == 'POST':
        session.delete(itemTypeToDelete)
        session.commit()
        return redirect(
            url_for('showItems', item_type_id=item_type_id))
    else:
        return render_template(
            'deleteItemType.html', item= itemTypeToDelete)
    # return 'This page will be for deleting item %s' % item_id


# Show a item menu
@app.route('/item/<int:item_type_id>/')
@app.route('/item/<int:item_type_id>/menu/')
def showMenu(item_type_id):
    item = session.query(ItemType).filter_by(id=item_type_id).one()
    items = session.query(MenuItem).filter_by(
        item_type_id=item_type_id).all()
    return render_template('menu.html', items=items, item=item)
    # return 'This page is the menu for item %s' % item_id

# Create a new menu item


@app.route(
    '/item/<int:item_type_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(item_type_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'], item_type_id=item_type_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showMenu', item_type_id=item_type_id))
    else:
        return render_template('newmenuitem.html', item_type_id=item_type_id)

    return render_template('newMenuItem.html', item=item)
    # return 'This page is for making a new menu item for item %s'
    # %item_id

# Edit a menu item


@app.route('/item/<int:item_type_id>/menu/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(item_type_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showMenu', item_type_id=item_type_id))
    else:

        return render_template(
            'editmenuitem.html', item_type_id=item_type_id, menu_id=menu_id, item=editedItem)

    # return 'This page is for editing menu item %s' % menu_id

# Delete a menu item


@app.route('/item/<int:item_type_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(item_type_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showMenu', item_type_id=item_type_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)
    # return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)