const projects = [
  {
    _id: 1,
    name: "Project 1",
    description: "This is a description for project 1",
    created_by: "Oscar",
    status: "NEW",
    last_updated: 2023 - 20 - 45,
  },
  {
    _id: 2,
    name: "Project 2",
    description: "This is a description for project 2",
    created_by: "Wunmi",
    status: "IN PROGRESS",
    last_updated: 2023 - 20 - 45,
  },
  {
    _id: 3,
    name: "Project 3",
    description: "This is a description for project 3",
    created_by: "Fatima",
    status: "CLOSED",
    last_updated: 2023 - 20 - 45,
  },
];

const bugs = [
  {
    _id: 1,
    title: "Bug 1",
    description: "This is a description for bug 1",
    steps_to_reproduce: "This is how to reproduce bug 1",
    priority: "HIGH",
    reporter: "Oscar",
    status: "NEW",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
  {
    _id: 2,
    title: "Bug 2",
    description: "This is a description for bug 2",
    steps_to_reproduce: "This is how to reproduce bug 2",
    priority: "MEDIUM",
    reporter: "Wunmi",
    status: "IN PROGRESS",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
  {
    _id: 3,
    title: "Bug 3",
    description: "This is a description for bug 3",
    steps_to_reproduce: "This is how to reproduce bug 3",
    priority: "LOW",
    reporter: "Fatima",
    status: "RESOLVED",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
  {
    _id: 4,
    title: "Bug 4",
    description: "This is a description for bug 4",
    steps_to_reproduce: "This is how to reproduce bug 4",
    priority: "URGENT",
    reporter: "Oscar",
    status: "CLOSED",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
  {
    _id: 5,
    title: "Bug 4",
    description: "This is a description for bug 5",
    steps_to_reproduce: "This is how to reproduce bug 5",
    priority: "IMMEDIATE",
    reporter: "Oscar",
    status: "NEW",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
  {
    _id: 6,
    title: "Bug 6",
    description: "This is a description for bug 6",
    steps_to_reproduce: "This is how to reproduce bug 6",
    priority: "CRITICAL",
    reporter: "Oscar",
    status: "IN PROGRESS",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
  {
    _id: 7,
    title: "Bug 7",
    description: "This is a description for bug 7",
    steps_to_reproduce: "This is how to reproduce bug 7",
    priority: "BLOCKER",
    reporter: "Oscar",
    status: "RESOLVED",
    last_updated: 2023 - 20 - 45,
    assigned_developer: "Ademola",
    assigner: "Ajike",
    project: 1,
  },
];

const comments = [
  {
    _id: 1,
    author: "Wunmi",
    content: "Lorem ipsum dolor amet si quando",
    bug: 1,
    created_at: "2023-20-45",
    updated_at: "2023-20-33",
  },
  {
    _id: 2,
    author: "Oscar",
    content: "Lorem ipsum dolor amet si quando",
    bug: 1,
    created_at: "2023-20-45",
    updated_at: "2023-20-33",
  },
  {
    _id: 3,
    author: "Campbell",
    content: "Lorem ipsum dolor amet si quando",
    bug: 2,
    created_at: "2023-20-45",
    updated_at: "2023-20-33",
  },
  {
    _id: 4,
    author: "Xavier",
    content: "Lorem ipsum dolor amet si quando",
    bug: 3,
    created_at: "2023-20-45",
    updated_at: "2023-20-33",
  },
  {
    _id: 5,
    author: "Ajike",
    content: "Lorem ipsum dolor amet si quando",
    bug: 4,
    created_at: "2023-20-45",
    updated_at: "2023-20-33",
  },
];

module.exports = { projects, bugs, comments };