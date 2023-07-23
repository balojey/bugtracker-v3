export default function Comment({ props }) {
  return (
    <div className="chat chat-start">
      <div className="chat-image avatar">
        <div className="w-10 rounded-full">
          <img src="https://api.dicebear.com/6.x/adventurer/svg?seed=Kitty" />
        </div>
      </div>
      <div className="chat-bubble rounded-none">{props.content}</div>
    </div>
  );
}
