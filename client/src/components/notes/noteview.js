import React, { Component } from "react";
import { withRouter } from "react-router";

//This component will render as a child of home on the
// /notes/%noteid route when the user is logged in.
//It presents the user with the note title and content
//as well as a paginated list of tags associated with it
//and its created and modified dates.  It also provides
//a form to edit the note.

//https://balsamiq.cloud/sc1hpyg/po5pcja/r9F28
class NoteView extends Component {
  render() {
    return (
      <div>
        <p>NOTEVIEW PLACEHOLDER</p>
      </div>
    );
  }
}

export default withRouter(NoteView);
