import Type from "./Type";

function Table({ headers, rows }) {
  return (
    <table className="api-table">
      <thead>
      <tr>
        {headers.map((header, index) => (
          <th key={index}>{header}</th>
        ))}
      </tr>
      </thead>
      <tbody>
      {rows.map((row, index) => (
        <tr key={index}>
          {row.map((cell, cellIndex) => (
            <td key={cellIndex}>{cell}</td>
          ))}
        </tr>
      ))}
      </tbody>
    </table>
  );
}

function renderSignature(signature) {
  return <code>{signature}</code>;
}

function renderType(type) {
  if (!type) return null;
  return <Type name={type}/>;
}

function renderAccess(access) {
  if (access === undefined) return null;

  if (access === true) return <code>get/set</code>;
  if (access === false) return <code>get</code>;

  return <code>{access}</code>;
}

export default function ApiDoc({
                                 constructors = [],
                                 attributes = [],
                                 virtualAttributes = [],
                                 methods = [],
                                 staticMethods = []
                               }) {
  return (
    <>
      {constructors.length > 0 && (
        <>
          <h2>Constructors</h2>
          <Table
            headers={["Signature", "Description"]}
            rows={constructors.map(c => [renderSignature(c.signature), c.description])}
          />
        </>
      )}

      {attributes.length > 0 && (
        <>
          <h2>Attributes</h2>
          <Table
            headers={["Name", "Type", "Description"]}
            rows={attributes.map(a => [<code>{a.name}</code>, renderType(a.type), a.description])}
          />
        </>
      )}

      {virtualAttributes.length > 0 && (
        <>
          <h2>Virtual Attributes</h2>
          <Table
            headers={["Name", "Type", "Access", "Description"]}
            rows={virtualAttributes.map(v => [
              <code>{v.name}</code>,
              renderType(v.type),
              renderAccess(v.access),
              v.description,
            ])}
          />
        </>
      )}

      {methods.length > 0 && (
        <>
          <h2>Methods</h2>
          <Table
            headers={["Signature", "Returns", "Description"]}
            rows={methods.map(m => [
              renderSignature(m.signature),
              renderType(m.returns),
              m.description,
            ])}
          />
        </>
      )}

      {staticMethods.length > 0 && (
        <>
          <h2>Static Methods</h2>
          <Table
            headers={["Signature", "Returns", "Description"]}
            rows={staticMethods.map(m => [
              renderSignature(m.signature),
              renderType(m.returns),
              m.description,
            ])}
          />
        </>
      )}
    </>
  );
}
