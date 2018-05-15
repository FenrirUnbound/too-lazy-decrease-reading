import React, { Component } from 'react';
import {
  Button,
  Col,
  ControlLabel,
  FormControl,
  FormGroup,
  Grid,
  Panel,
  Row
} from 'react-bootstrap';
import logo from './logo.svg';
import axios from 'axios';

const Summary = (props) => {
  let content = [];

  if (props.data.summary) {
    content = props.data.summary.map((line, index) => (
      <p key={`sumline_${index}`}>
        {line}
      </p>
    ));
  }

  return (
    <Panel>
      <Panel.Heading>
        <Panel.Title>Summary</Panel.Title>
      </Panel.Heading>
      <Panel.Body>
        {content}
      </Panel.Body>
    </Panel>
  );
};

class UserInput extends Component {
  constructor(props) {
    super(props);

    this.state = {
      textVal: ''
    };
  }

  submitArticle(event) {
    event.preventDefault();

    this.props.submitArticle(this.state.textVal);
  }

  updateText(event) {
    this.setState({
      textVal: event.target.value
    });
  }

  render() {
    const placeholder = 'Past text in this box and hit it!';

    return (
      <form onSubmit={(e) => this.submitArticle(e)}>
        <FormGroup controlId="formControlsTextarea">
          <ControlLabel>Article</ControlLabel>
          <FormControl
            componentClass="textarea"
            placeholder={placeholder}
            value={this.state.textVal}
            onChange={(e) => this.updateText(e)}/>
        </FormGroup>

        <Button
          bsSize="large"
          type="submit"
          disabled={this.state.textVal.length === 0}
          block>Submit</Button>
      </form>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      summary: ''
    };
  }

  async submitArticle(text) {
    try {
      const summary = await axios.post('/api/summarize', { data: text });

      this.setState({ summary: summary.data });
    } catch(e) {
      console.error(`Error encountered while sending text to summary API: ${JSON.stringify(e)}`);
    }
  }

  render() {
    const spacing = { marginTop: '5em' };
    const hideSummary = (this.state.summary) ? {} : {display: 'none'};

    return (
      <Grid>
        <Row>
          <Col md={8} mdOffset={2}>
            <h1 className="text-center">Too Lazy; Decrease Reading</h1>
          </Col>
        </Row>
        <Row>
          <Col md={8} mdOffset={2}>
            <UserInput submitArticle={this.submitArticle.bind(this)}/>
          </Col>
        </Row>
        <Row style={spacing}>
          <Col md={8} mdOffset={2} style={hideSummary}>
            <Summary data={this.state.summary}/>
          </Col>
        </Row>
      </Grid>
    );
  }
}

export default App;
