export default function UploadCard({
    title,
    description,
    icon,
    onClick,
}) {
    return (
        <button
            onClick={onClick}
            className="
                w-full
                bg-white
                rounded-2xl
                shadow-md
                p-6
                text-left
                hover:shadow-lg
                hover:border-emerald-500
                border-2
                border-transparent
                transition
            "
        >
            <div className="text-4xl mb-4">
                {icon}
            </div>

            <h2 className="text-2xl font-bold">
                {title}
            </h2>

            <p className="text-slate-600 mt-2">
                {description}
            </p>
        </button>
    );
}