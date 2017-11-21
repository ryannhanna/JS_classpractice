import React, { Component } from 'react';
import PropTypes from 'prop-types';


class ProjectItem extends Component {
  deleteProject(id){
    this.props.onDelete(id);

  }

  render() {
    return (
      <li className="Projects">
      <strong>{this.props.project.title}</strong>: - {this.props.project.category} <a href="#" onClick={this.deleteProject.bind(this, this.props.project.id)}>x</a>
    </li>
    );
  }
}

ProjectItem.propTypes = {
project: React.PropTypes.object,
onDelete: React.PropTypes.func

}

export default ProjectItem;
