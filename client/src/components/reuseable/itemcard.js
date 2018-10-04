import React, { Component } from "react";
import { withRouter } from "react-router";
import { Link } from "react-router-dom";
import { Create, Delete } from "@material-ui/icons";
import { IconButton, Typography, Dialog } from "@material-ui/core";
import { DeleteItem } from "..";
import "./itemcard.css";

//  This component will render as a child of the card list component.
//  It presents a small area of preview information for an individual item.
//  Displays the item name as well as edit and delete buttons.

//  PROPS:
//    item: The item to be displayed.
//    type: The item's type.

//https://balsamiq.cloud/sc1hpyg/po5pcja/r0C2B
class ItemCard extends Component {
  constructor() {
    super();
    this.state = {
      deleting: false
    };
  }

  handleDeleteButton = () => {
    this.setState({ deleting: true });
  };

  cancelDelete = () => {
    this.setState({ deleting: false });
  };

  render() {
    let path = "";
    let name = "";
    switch (this.props.type) {
      case "job":
        path = "/jobs";
        name = this.props.item.name;
        break;
      case "client":
        path = "/clients";
        if (this.props.item.businessName) name = this.props.item.businessName;
        else name = `${this.props.item.firstName} ${this.props.item.lastName}`;
        break;
      case "note":
        path = "/notes";
        name = this.props.item.title;
        break;
      case "tag":
        path = "/tags";
        name = this.props.item.name;
        break;
      case "part":
        path = "/parts";
        name = this.props.item.name;
      default:
        break;
    }
    return (
      <div className="item-card">
        <div className="item-card-icons">
          <Link to={`${path}/${this.props.item.id}/edit`}>
            <IconButton>
              <Create />
            </IconButton>
          </Link>
          <IconButton onClick={this.handleDeleteButton}>
            <Delete />
          </IconButton>
        </div>
        <h4 className="item-card-name">
          <Link to={`${path}/${this.props.item.id}`}>
            <Typography variant="title" noWrap>
              {name}
            </Typography>
          </Link>
        </h4>
        <Dialog
          open={this.state.deleting}
          onClose={this.cancelDelete}
          className="delete-modal"
        >
          <DeleteItem
            cancelDelete={this.cancelDelete}
            type={this.props.type}
            item={this.props.item}
            after_path={path}
          />
        </Dialog>
      </div>
    );
  }
}

export default withRouter(ItemCard);
