export default function Button({ children, onClick, disabled, className }) {
    return (
      <button
        onClick={onClick}
        disabled={disabled}
        className={`px-4 py-2 bg-blue-600 text-white rounded-md ${className}`}
      >
        {children}
      </button>
    );
  }
  